from pydantic import BaseModel


class BookEntry(BaseModel):
    Title: str
    Author: str
    Year: int
    Description: str
    Text: str
    ImageUrl: str
    Url: str
