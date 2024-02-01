from typing import List
from src.Code import BookEntry


def CreateSampleBooks() -> List[BookEntry]:
    books = [
        BookEntry.BookEntry(
            Title="The Great Gatsby",
            Author="F. Scott Fitzgerald",
            Year=1925,
            Description="The Great Gatsby is a novel by American author F. Scott Fitzgerald. The story takes place in 1922, during the Roaring Twenties, a time of prosperity in the United States after World War I. The book received critical acclaim and is generally considered Fitzgerald's best work. It is also widely regarded as a Great American Novel and a literary classic, capturing the essence of an era.",
            Text="The Great Gatsby is a novel by American author F. Scott Fitzgerald. The story takes place in 1922, during the Roaring Twenties, a time of prosperity in the United States after World War I. The book received critical acclaim and is generally considered Fitzgerald's best work. It is also widely regarded as a Great American Novel and a literary classic, capturing the essence of an era.",
            ImageUrl="https://upload.wikimedia.org/wikipedia/commons/f/f7/TheGreatGatsby_1925jacket.jpeg",
            Url="https://en.wikipedia.org/wiki/The_Great_Gatsby"
        ),
        BookEntry.BookEntry(
            Title="To Kill a Mockingbird",
            Author="Harper Lee",
            Year=1960,
            Description="To Kill a Mockingbird is a novel by the American author Harper Lee. It was published in 1960 and has become a classic of modern American literature. The novel is loosely based on the author's observations of her family and neighbors, as well as an event that occurred near her hometown in 1936, when she was 10 years old.",
            Text="To Kill a Mockingbird is a novel by the American author Harper Lee. It was published in 1960 and has become a classic of modern American literature. The novel is loosely based on the author's observations of her family and neighbors, as well as an event that occurred near her hometown in 1936, when she was 10 years old.",
            ImageUrl="https://upload.wikimedia.org/wikipedia/commons/4/4f/To_Kill_a_Mockingbird_%28first_edition_cover%29.jpg",
            Url="https://en.wikipedia.org/wiki/To_Kill_a_Mockingbird"
        )]

    return books
