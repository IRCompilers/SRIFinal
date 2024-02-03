from fastapi import FastAPI

from src.Code.Recommendation.RecommendationSystem import BookRecommendationSystem

app = FastAPI()

# Create an instance of BookRecommendationSystem
book_rec_system = BookRecommendationSystem()


@app.get("/query")
def query_books(query: str):
    # Use the instance method Query of book_rec_system
    return book_rec_system.Query(query)
