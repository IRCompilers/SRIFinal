from fastapi import FastAPI

from src.Code.Recommendation.RecommendationSystem import BookRecommendationSystem
from src.Code.Recommendation.Sampler import CreateSampleBooks

app = FastAPI()

# Create an instance of BookRecommendationSystem
book_rec_system = BookRecommendationSystem()


@app.get("/query")
def query_books(query: str):
    # Use the instance method Query of book_rec_system
    return book_rec_system.Query(query)


@app.get("/autocomplete")
def auto_complete(query: str):
    # Use the instance method AutoComplete of book_rec_system
    return book_rec_system.AutoComplete(query)


@app.get("/sample")
def sample():
    books = CreateSampleBooks()
    book_rec_system.AddBooks(books)
    book_rec_system.LoadResources()
