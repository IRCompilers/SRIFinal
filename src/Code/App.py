from fastapi import FastAPI, HTTPException

from src.Code.Models.BookEntry import BookEntry
from src.Code.Recommendation.RecommendationSystem import BookRecommendationSystem
from src.Code.Recommendation.Sampler import CreateSampleBooks, GetRandomBook

app = FastAPI()
book_rec_system = BookRecommendationSystem()


@app.get("/query")
def query_books(query: str):
    """
    Query books based on the provided query string.

    Args:
        query (str): The query string to search for in the books.

    Returns:
        list: A list of books that match the query string.
    """
    return book_rec_system.Query(query)


@app.get("/autocomplete")
def auto_complete(query: str):
    """
    Autocomplete the query based on the provided query string.

    Args:
        query (str): The query string to autocomplete.

    Returns:
        list: A list of possible completions for the query string.
    """
    return book_rec_system.AutoComplete(query)


@app.get("/sample")
def sample():
    """
    Create sample books and load them into the recommendation system.

    Returns:
        None
    """
    books = CreateSampleBooks()
    book_rec_system.AddBooks(books)
    book_rec_system.LoadResources()


@app.get("/add-single")
def addSingle():
    book = GetRandomBook()
    book_rec_system.AddBook(book)


@app.post("/add-book")
def add_book(book: BookEntry):
    """
    Add a new book to the recommendation system.

    Args:
        book (BookEntry): The book to add.

    Returns:
        dict: A message indicating the result of the operation.
    """
    try:
        book_rec_system.AddBook(book)
        return {"message": "Book added successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
