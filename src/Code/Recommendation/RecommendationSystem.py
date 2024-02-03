# Python imports
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from typing import List

# External imports
from gensim import similarities, corpora

# Internal imports
from src.Code.Models import BookEntry
from src.Code.Models.BookCard import BookCard
from src.Code.Recommendation.Preprocessor import Preprocess
from src.Code.Recommendation.Serializer import SaveBooksToJson, LoadBooksFromJson
from src.Code.Recommendation.Vectorizer import Vectorize


class BookRecommendationSystem:
    def __init__(self):
        self.dictionary = None
        self.book_buckets = None

    @staticmethod
    @lru_cache(maxsize=None)
    def AddBooks(books: List[BookEntry]):
        texts = [book.Text for book in books]
        preprocessed_documents = Preprocess(texts)
        vectorized_documents, dictionary = Vectorize(preprocessed_documents)
        SaveBooksToJson(books, vectorized_documents, '../../books.json')
        dictionary.save('../../dictionary.pkl')

    def load_resources(self):
        if self.book_buckets is None:
            self.book_buckets = LoadBooksFromJson('books.json')
        if self.dictionary is None:
            self.dictionary = corpora.Dictionary.load('dictionary.pkl')

    def Query(self, query: str) -> List[BookCard]:
        self.load_resources()

        preprocessed_query = Preprocess([query])
        query_vector, _ = Vectorize(preprocessed_query, self.dictionary, True)

        index = similarities.MatrixSimilarity([bucket.Vector for bucket in self.book_buckets])
        sims = index[query_vector]

        with ThreadPoolExecutor() as executor:
            book_cards = list(executor.map(self.create_book_card, enumerate(sims[0])))

        book_cards = [book_card for book_card in book_cards if book_card is not None]

        book_cards = sorted(book_cards, key=lambda x: x.Rating, reverse=True)

        return book_cards

    def create_book_card(self, sim_tuple):
        i, sim = sim_tuple
        if sim > 0.0:
            return BookCard(
                Title=self.book_buckets[i].Title,
                Author=self.book_buckets[i].Author,
                Year=self.book_buckets[i].Year,
                Description=self.book_buckets[i].Description,
                ImageUrl=self.book_buckets[i].ImageUrl,
                Rating=sim * 5.0,
                Url=self.book_buckets[i].Url,
                Tags=[]
            )
        return None
