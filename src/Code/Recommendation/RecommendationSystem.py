from typing import List

from gensim import similarities, corpora

from src.Code.Models import BookEntry
from src.Code.Models.BookCard import BookCard
from src.Code.Recommendation.Preprocessor import Preprocess
from src.Code.Recommendation.Serializer import SaveBooksToJson, LoadBooksFromJson
from src.Code.Recommendation.Vectorizer import Vectorize


class BookRecommendationSystem:
    def __init__(self):
        pass

    @staticmethod
    def AddBooks(books: List[BookEntry]):
        texts = [book.Text for book in books]
        preprocessed_documents = Preprocess(texts)
        vectorized_documents, dictionary = Vectorize(preprocessed_documents)
        SaveBooksToJson(books, vectorized_documents, '../../books.json')
        dictionary.save('../../dictionary.pkl')

    @staticmethod
    def Query(query: str) -> List[BookCard]:
        # Load the book buckets from the JSON file
        book_buckets = LoadBooksFromJson('books.json')

        # Load the dictionary
        dictionary = corpora.Dictionary.load('dictionary.pkl')

        # Preprocess the query string
        preprocessed_query = Preprocess([query])
        # Vectorize the preprocessed query
        query_vector, _ = Vectorize(preprocessed_query, dictionary, True)

        # Calculate the similarity between the query vector and each book vector
        index = similarities.MatrixSimilarity([bucket.Vector for bucket in book_buckets])
        sims = index[query_vector]

        book_cards = [BookCard(
            Title=book_buckets[i].Title,
            Author=book_buckets[i].Author,
            Year=book_buckets[i].Year,
            Description=book_buckets[i].Description,
            ImageUrl=book_buckets[i].ImageUrl,
            Rating=sim * 5.0,
            Url=book_buckets[i].Url,
            Tags=[]
        ) for i, sim in enumerate(sims[0]) if sim > 0.0]

        # Sort the book cards by rating in descending order
        book_cards = sorted(book_cards, key=lambda x: x.Rating, reverse=True)

        return book_cards
