# Python imports
from concurrent.futures import ThreadPoolExecutor
from typing import List

# External imports
from gensim import similarities, corpora

# Internal imports
from src.Code.Models import BookEntry
from src.Code.Models.BookCard import BookCard
from src.Code.Recommendation.Preprocessor import Preprocess
from src.Code.Recommendation.Serializer import SaveBooksToJson, LoadBooksFromJson, SaveTrieToJson, LoadTrieFromJson
from src.Code.Recommendation.Tagger import PredictTags
from src.Code.Recommendation.Vectorizer import Vectorize
from src.Code.Trie.Trie import Trie


def flatten_list(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]


class BookRecommendationSystem:
    def __init__(self):
        self.dictionary = None
        self.book_buckets = None
        self.autocomplete = Trie()
        self.LoadResources()

    @staticmethod
    def AddBooks(books: List[BookEntry]):
        texts = [book.Text for book in books]
        preprocessed_documents = Preprocess(texts)
        trie = Trie()

        for word in flatten_list(preprocessed_documents):
            trie.Insert(word)

        SaveTrieToJson(trie, "Resources/autocomplete_trie.json")

        tags = BookRecommendationSystem.predict_tags_parallel(preprocessed_documents)
        vectorized_documents, dictionary = Vectorize(preprocessed_documents)
        SaveBooksToJson(books, vectorized_documents, tags, 'Resources/books.json')
        dictionary.save('Resources/dictionary.pkl')

    @staticmethod
    def predict_tags_parallel(corpus_descriptions: List[List[str]]):
        # Extract descriptions from books
        descriptions = [description for description in corpus_descriptions]

        # Create a ThreadPoolExecutor
        with ThreadPoolExecutor() as executor:
            # Use the executor to map the predict_tags function to the descriptions
            predicted_tags = list(executor.map(PredictTags, descriptions))

        return predicted_tags

    def LoadResources(self):
        print("Loading resources")
        try:
            if self.book_buckets is None:
                self.book_buckets = LoadBooksFromJson('Resources/books.json')
            if self.dictionary is None:
                self.dictionary = corpora.Dictionary.load('Resources/dictionary.pkl')
            if len(self.autocomplete.root.children) == 0:
                LoadTrieFromJson(self.autocomplete, 'Resources/autocomplete_trie.json')
        except FileNotFoundError:
            print("Error loading resources - Files where not found. Please add books to the system first.")

    def Query(self, query: str) -> List[BookCard]:
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

    def AutoComplete(self, query):
        return self.autocomplete.MostCommon(query)
