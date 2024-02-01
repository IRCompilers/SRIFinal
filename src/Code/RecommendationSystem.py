from typing import List

from src.Code import BookEntry
from src.Code.Preprocessor import Preprocess
from src.Code.Sampler import CreateSampleBooks
from src.Code.Vectorizer import Vectorize


def AddBooks(books: List[BookEntry]):
    texts = [book.Text for book in books]

    preprocessed_documents = Preprocess(texts)
    for doc in preprocessed_documents:
        print(doc)


    vectorized_documents = Vectorize(preprocessed_documents)

    for i, tf_idf in enumerate(vectorized_documents):
       print(tf_idf)


books = CreateSampleBooks()
AddBooks(books)
