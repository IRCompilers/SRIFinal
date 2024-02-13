import json
import re
from typing import Any

from fastapi import FastAPI, HTTPException

from src.Code.Models.BookEntry import BookEntry
from src.Code.Recommendation.RecommendationSystem import BookRecommendationSystem
from src.Code.Recommendation.Sampler import CreateSampleBooks, GetRandomBook
from src.Code.Recommendation.Tagger import TrainModel

app = FastAPI()
book_rec_system = BookRecommendationSystem()


@app.get("/query")
def query_books(query: str, page: int = 0, pageSize: int = 10, previouslyRead: str = ''):
    """
    Query books based on the provided query string and previously read books.

    Args:
        query (str): The query string to search for in the books.
        previouslyRead (str): A string of comma-separated book titles that the user has previously read.
        page (int): The page number for pagination. Each page contains pageSize results.
        pageSize (int): The number of results to return per page.

    Returns:
        page: A list of books that match the query string and a total amount of results.
    """

    page = page - 1
    previously_read_books = [book.strip() for book in previouslyRead.split(',')] if previouslyRead else []
    all_results = book_rec_system.Query(query, previously_read_books)
    paginated_results = all_results[page * pageSize:(page + 1) * pageSize]
    return {"results": paginated_results, "total": len(all_results)}


@app.get("/autocomplete")
def auto_complete(query: str, is_book: bool = False):
    """
    Autocomplete the query based on the provided query string.

    Args:
        query (str): The query string to autocomplete.
        is_book (bool): If the query is to autocomplete books or not

    Returns:
        list: A list of possible completions for the query string.
    """
    return book_rec_system.AutoComplete(query, is_book)


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


@app.get("/populate")
def populate() -> Any:
    """
    Read from the known_books.json file in the Content folder and output it to a variable.

    Returns:
        Any: The content of the known_books.json file.
    """
    with open('Content/known_books.json', 'r') as file:
        data = json.load(file)

    descriptions = [book['description'] for book in data]
    tags = [json.loads(book['genres'].replace('\'', '\"')) for book in data]

    TrainModel(descriptions, tags)

    with open('Content/data.json', 'r') as file:
        book_file = json.load(file)

    books = []
    for book_data in book_file:
        book = BookEntry(
            Description=book_data['description'],
            Title=book_data['title'],
            Author=book_data['author'],
            Year=book_data['year'],
            ImageUrl=book_data.get('image', ''),
            Url=''
        )
        books.append(book)

    book_rec_system.AddBooks(books)
    book_rec_system.LoadResources()

    return {'message': 'ok'}



