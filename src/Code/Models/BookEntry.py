from dataclasses import dataclass


@dataclass
class BookEntry:
    Title: str
    Author: str
    Year: int
    Description: str
    Text: str
    ImageUrl: str
    Url: str
