import json
from typing import List

from src.Code.Models import BookEntry
from src.Code.Models.BookBucket import BookBucket


def SaveBooksToJson(books: List[BookEntry], vectorized_documents, tags, filename: str):
    """
    Save the given books, vectorized documents, and tags to a JSON file.

    Args:
        books (List[BookEntry]): The list of books to save.
        vectorized_documents (list): The list of vectorized documents to save.
        tags (list): The list of tags to save.
        filename (str): The name of the file to save to.
    """
    book_buckets = []
    for book, vector, tags in zip(books, vectorized_documents, tags):
        book_bucket = BookBucket(
            Title=book.Title,
            Author=book.Author,
            Year=book.Year,
            Description=book.Description,
            ImageUrl=book.ImageUrl,
            Tags=[tags[0]],
            Url=book.Url,
            Vector=vector
        )
        book_buckets.append(book_bucket.to_dict())

    with open(filename, 'w') as f:
        json.dump(book_buckets, f)


def LoadBooksFromJson(filename: str) -> List[BookBucket]:
    """
    Load book buckets from a JSON file.

    Args:
        filename (str): The name of the file to load from.

    Returns:
        List[BookBucket]: A list of book buckets loaded from the file.
    """
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
            Tags=book_dict["Tags"],
            Vector=book_dict["Vector"]
        )
        book_buckets.append(book_bucket)

    return book_buckets


def SaveTrieToJson(trie, filename: str):
    """
    Save the given MCS Trie to a JSON file.

    Args:
        trie (Trie): The trie to save.
        filename (str): The name of the file to save to.
    """
    with open(filename, 'w') as f:
        json.dump(trie.to_dict(), f)


def LoadTrieFromJson(trie, filename: str):
    """
    Load an MCS Trie from a JSON file.

    Args:
        trie (Trie): The trie to load into.
        filename (str): The name of the file to load from.

    Returns:
        Trie: The loaded trie.
    """
    with open(filename, 'r') as f:
        data = json.load(f)

    return trie.from_dict(data)
