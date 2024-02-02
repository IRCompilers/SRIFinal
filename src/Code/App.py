from fastapi import FastAPI

from src.Code.RecommendationSystem import Query

app = FastAPI()


@app.get("/query")
def query_books(query: str):
    return Query(query)
