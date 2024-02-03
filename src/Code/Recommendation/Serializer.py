import json
from typing import List

from src.Code.Models import BookEntry
from src.Code.Models.BookBucket import BookBucket


def SaveBooksToJson(books: List[BookEntry], vectorized_documents, filename: str):
    book_buckets = []
    for book, vector in zip(books, vectorized_documents):
        book_bucket = BookBucket(
            Title=book.Title,
            Author=book.Author,
            Year=book.Year,
            Description=book.Description,
            ImageUrl=book.ImageUrl,
            Url=book.Url,
            Vector=vector
        )
        book_buckets.append(book_bucket.to_dict())

    with open(filename, 'w') as f:
        json.dump(book_buckets, f)


def LoadBooksFromJson(filename: str) -> List[BookBucket]:
    with open(filename, 'r') as f:
        data = json.load(f)

    book_buckets = []
    for book_dict in data:
        book_bucket = BookBucket(
            Title=book_dict["Title"],
            Author=book_dict["Author"],
            Year=book_dict["Year"],
            Description=book_dict["Description"],
            ImageUrl=book_dict["ImageUrl"],
            Url=book_dict["Url"],
            Vector=book_dict["Vector"]
        )
        book_buckets.append(book_bucket)

    return book_buckets


def SaveTrieToJson(trie, filename: str):
    with open(filename, 'w') as f:
        json.dump(trie.to_dict(), f)


def LoadTrieFromJson(trie, filename: str):
    with open(filename, 'r') as f:
        data = json.load(f)

    return trie.from_dict(data)
