from fastapi import FastAPI

from src.Code.Recommendation.RecommendationSystem import BookRecommendationSystem

app = FastAPI()


@app.get("/query")
def query_books(query: str):
    return BookRecommendationSystem.Query(query)
