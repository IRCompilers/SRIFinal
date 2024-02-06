from pydantic import BaseModel


class BookEntry(BaseModel):
    Title: str
    Author: str
    Year: int
    Description: str
    ImageUrl: str
    Url: str
