from dataclasses import field, dataclass
from typing import List


@dataclass
class BookBucket:
    Title: str
    Author: str
    Year: int
    Description: str
    ImageUrl: str
    Url: str
    Tags: List[str] = field(default_factory=list)
    Vector: List[float] = field(default_factory=list)

    def to_dict(self):
        return {
            "Title": self.Title,
            "Author": self.Author,
            "Year": self.Year,
            "Description": self.Description,
            "ImageUrl": self.ImageUrl,
            "Url": self.Url,
            "Tags": self.Tags,
            "Vector": self.Vector
        }
