from typing import List

from gensim import similarities, corpora

from src.Code import BookEntry
from src.Code.BookCard import BookCard
from src.Code.Preprocessor import Preprocess
from src.Code.Sampler import CreateSampleBooks
from src.Code.Serializer import SaveBooksToJson, LoadBooksFromJson
from src.Code.Vectorizer import Vectorize


def AddBooks(books: List[BookEntry]):
    texts = [book.Text for book in books]
    preprocessed_documents = Preprocess(texts)
    vectorized_documents, dictionary = Vectorize(preprocessed_documents)
    SaveBooksToJson(books, vectorized_documents, 'books.json')
    dictionary.save('dictionary.pkl')


def Query(query: str) -> List[BookCard]:
    # Load the book buckets from the JSON file
    book_buckets = LoadBooksFromJson('books.json')

    # Load the dictionary
    dictionary = corpora.Dictionary.load('dictionary.pkl')

    # for id, token in dictionary.items():
    #     print(f"ID: {id}, Token: {token}")

    # Preprocess the query string
    preprocessed_query = Preprocess([query])

    print("Preprocessed query: ", preprocessed_query)
    for word in preprocessed_query[0]:
        if word in dictionary.token2id:
            print(f"'{word}' is in the dictionary with id {dictionary.token2id[word]}")
        else:
            print(f"'{word}' is not in the dictionary")

    # Vectorize the preprocessed query
    query_vector, _ = Vectorize(preprocessed_query, dictionary)

    for v in query_vector:
        print(v)

    # Calculate the similarity between the query vector and each book vector
    index = similarities.MatrixSimilarity([bucket.Vector for bucket in book_buckets])

    # print("Query vector", list(query_vector))

    sims = index[query_vector]

    for i in range(len(sims)):
        print(f"Book {i} has similarity score {sims[i]}")

    # Sort the books by their similarity scores
    sorted_book_buckets = sorted(zip(book_buckets, sims), key=lambda item: -item[1])

    # Convert the sorted book buckets into BookCard objects
    book_cards = [BookCard(
        Title=bucket.Title,
        Author=bucket.Author,
        Year=bucket.Year,
        Description="",
        ImageUrl=bucket.ImageUrl,
        Rating=sim,
        Url=bucket.Url,
        Tags=[]
    ) for bucket, sim in sorted_book_buckets]

    return book_cards


# books = CreateSampleBooks()
# AddBooks(books)
results = Query("Great grapes in this novel")
# print(results)
