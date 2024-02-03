from dataclasses import dataclass, field
from typing import List


@dataclass
class BookCard:
    Title: str
    Author: str
    Year: int
    Description: str
    ImageUrl: str
    Url: str
    Rating: float
    Tags: List[str] = field(default_factory=list)

    def to_dict(self):
        return {
            "Title": self.Title,
            "Author": self.Author,
            "Year": self.Year,
            "Description": self.Description,
            "ImageUrl": self.ImageUrl,
            "Url": self.Url,
            "Rating": self.Rating,
            "Tags": self.Tags
        }
