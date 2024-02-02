from typing import List

from src.Code import BookEntry
from src.Code.Preprocessor import Preprocess
from src.Code.Sampler import CreateSampleBooks
from src.Code.Vectorizer import Vectorize
from src.Code.Serializer import SaveBooksToJson, LoadBooksFromJson


def AddBooks(books: List[BookEntry]):
    texts = [book.Text for book in books]
    preprocessed_documents = Preprocess(texts)
    vectorized_documents = Vectorize(preprocessed_documents)
    SaveBooksToJson(books, vectorized_documents, 'books.json')


def Query(query: str):
    buckets = LoadBooksFromJson('books.json')
    print(buckets)


Query("The Hobbit")

# books = CreateSampleBooks()
# AddBooks(books)
