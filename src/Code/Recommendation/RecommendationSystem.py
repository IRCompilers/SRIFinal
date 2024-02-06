# Python imports
from concurrent.futures import ThreadPoolExecutor
from typing import List

# External imports
from gensim import similarities, corpora

# Internal imports
from src.Code.Models import BookEntry
from src.Code.Models.BookBucket import BookBucket
from src.Code.Models.BookCard import BookCard
from src.Code.Recommendation.Preprocessor import Preprocess
from src.Code.Recommendation.Serializer import SaveBooksToJson, LoadBooksFromJson, SaveTrieToJson, LoadTrieFromJson
from src.Code.Recommendation.Tagger import PredictTags
from src.Code.Recommendation.Vectorizer import Vectorize
from src.Code.Trie.Trie import Trie


def flatten_list(list_of_lists):
    """
    Flatten a list of lists into a single list.

    Args:
        list_of_lists (list): The list of lists to flatten.

    Returns:
        list: A flattened list.
    """
    return [item for sublist in list_of_lists for item in sublist]


class BookRecommendationSystem:
    """
    A class used to represent a Book Recommendation System.

    Attributes
    ----------
    dictionary : corpora.Dictionary
        a dictionary that maps each word to its "id"
    book_buckets : list
        a list of book buckets
    autocomplete : Trie
        a Trie data structure for autocomplete functionality
    autocomplete-books : Trie
        a Trie data structure for autocomplete functionality for books

    Methods
    -------
    AddBooks(books: List[BookEntry])
        Adds books to the system.
    PredictTagsInParallel(corpus_descriptions: List[List[str]]) -> List[List[str]]
        Predicts tags for the given corpus descriptions in parallel.
    LoadResources()
        Loads resources from the file system.
    Query(query: str) -> List[BookCard]
        Queries the system with the given query string.
    CreateBookCard(sim_tuple: (int, float)) -> BookCard | None
        Creates a book card from the given similarity tuple.
    AutoComplete(query: str) -> str
        Returns the most common autocomplete suggestions for the given query string.
    """

    def __init__(self):
        self.dictionary = None
        self.book_buckets = None
        self.autocomplete = Trie()
        self.autocomplete_books = Trie()
        self.LoadResources()

    @staticmethod
    def AddBooks(books: List[BookEntry]):
        """
            Adds books to the system.

            Args:
                books (List[BookEntry]): The list of books to add.
        """
        texts = [book.Description for book in books]
        preprocessed_documents = Preprocess(texts)
        trie = Trie()

        for word in flatten_list(preprocessed_documents):
            trie.Insert(word)

        booksTrie = Trie()
        for title in [book.Title for book in books]:
            booksTrie.Insert(title)

        SaveTrieToJson(trie, "Resources/autocomplete_trie.json")
        SaveTrieToJson(booksTrie, "Resources/autocomplete_books_trie.json")

        tags = BookRecommendationSystem.PredictTagsInParallel(preprocessed_documents)

        vectorized_documents, dictionary = Vectorize(preprocessed_documents)
        SaveBooksToJson(books, vectorized_documents, tags, 'Resources/books.json')
        dictionary.save('Resources/dictionary.pkl')

    def AddBook(self, book: BookEntry):
        """
        Adds a book to the system.

        Args:
            book (BookEntry): The book to add.
        """
        # Preprocess the book text
        books_texts = [bucket.Description for bucket in self.book_buckets]
        books_texts.append(book.Description)

        preprocessed_text = Preprocess(books_texts)

        # Insert each word of the preprocessed text into the autocomplete trie
        for word in preprocessed_text[-1]:
            self.autocomplete.Insert(word)

        # Predict the tags for the book
        tags = self.PredictTagsInParallel(preprocessed_text)

        # Vectorize the preprocessed text
        vectorized_text, _ = Vectorize(preprocessed_text, self.dictionary)

        # Create a new BookBucket object with the book details, vectorized text, and predicted tags
        book_bucket = BookBucket(
            Title=book.Title,
            Author=book.Author,
            Year=book.Year,
            Description=book.Description,
            ImageUrl=book.ImageUrl,
            Tags=tags[-1],
            Url=book.Url,
            Vector=vectorized_text[-1]
        )

        self.book_buckets.append(book_bucket)

        # Save the updated book_buckets list, dictionary, and autocomplete trie to the disk
        SaveBooksToJson(self.book_buckets, [bucket.Vector for bucket in self.book_buckets],
                        [bucket.Tags for bucket in self.book_buckets], 'Resources/books.json')
        self.dictionary.save('Resources/dictionary.pkl')
        SaveTrieToJson(self.autocomplete, 'Resources/autocomplete_trie.json')

    @staticmethod
    def PredictTagsInParallel(corpus_descriptions: List[List[str]]) -> List[List[str]]:
        """
            Predicts tags for the given corpus descriptions in parallel.

            Args:
                corpus_descriptions (List[List[str]]): The list of corpus descriptions.

            Returns:
                list: A list of predicted tags.
        """
        descriptions = [description for description in corpus_descriptions]

        # Create a ThreadPoolExecutor
        with ThreadPoolExecutor() as executor:
            # Use the executor to map the predict_tags function to the descriptions
            predicted_tags = list(executor.map(PredictTags, descriptions))

        return predicted_tags

    def LoadResources(self):
        """
            Loads resources from the recommendation system.
        """
        print("Loading resources")
        try:
            if self.book_buckets is None:
                self.book_buckets = LoadBooksFromJson('Resources/books.json')
            if self.dictionary is None:
                self.dictionary = corpora.Dictionary.load('Resources/dictionary.pkl')
            if len(self.autocomplete.root.children) == 0:
                LoadTrieFromJson(self.autocomplete, 'Resources/autocomplete_trie.json')
            if len(self.autocomplete_books.root.children) == 0:
                LoadTrieFromJson(self.autocomplete_books, 'Resources/autocomplete_books_trie.json')
        except FileNotFoundError:
            print("Error loading resources - Files where not found. Please add books to the system first.")

    def Query(self, query: str, previously_read_books: List[str]) -> List[BookCard]:
        """
        Queries the system with the given query string. Uses matrix cosine similarity to find the most similar books.

        Args:
            query (str): The query string.
            previously_read_books (str): A list of book titles that the user has previously read.

        Returns:
            List[BookCard]: A list of book cards that match the query string.
        """
        preprocessed_query = Preprocess([query])
        query_vector, _ = Vectorize(preprocessed_query, self.dictionary, True)

        index = similarities.MatrixSimilarity([bucket.Vector for bucket in self.book_buckets])
        sims = index[query_vector]

        self.HandlePreviouslyReadBooks(previously_read_books, sims[0])

        with ThreadPoolExecutor() as executor:
            book_cards = list(executor.map(self.CreateBookCard, enumerate(sims[0])))

        book_cards = [book_card for book_card in book_cards if
                      book_card is not None and book_card.Title not in previously_read_books]

        book_cards = sorted(book_cards, key=lambda x: x.Rating, reverse=True)

        return book_cards

    def HandlePreviouslyReadBooks(self, previously_read_books: list, similarities: dict):
        """
        Increase the similarity scores for books with tags that match those of the previously read books.

        Args:
            previously_read_books (list): A list of book titles that the user has previously read.
            similarities (dict): A dictionary of similarity scores for each book.
        """
        tag_counts = {}

        for book in self.book_buckets:
            if book.Title in previously_read_books:
                for tag in book.Tags:
                    tag_counts[tag] = tag_counts.get(tag, 0) + 1

        for i in range(len(self.book_buckets)):
            book = self.book_buckets[i]
            for tag in book.Tags:
                if tag in tag_counts:
                    similarities[i] += (tag_counts[tag] * 0.3)

    def CreateBookCard(self, sim_tuple: (int, float)) -> BookCard | None:
        """
        Creates a book card from the given similarity tuple, containing the index of the book and the similarity rating.

        Args:
            sim_tuple (tuple): The similarity tuple.

        Returns:
            BookCard: A book card.
        """
        i, sim = sim_tuple
        if sim > 0.0:
            return BookCard(
                Title=self.book_buckets[i].Title,
                Author=self.book_buckets[i].Author,
                Year=self.book_buckets[i].Year,
                Description=self.book_buckets[i].Description,
                ImageUrl=self.book_buckets[i].ImageUrl,
                Rating=sim * 5.0,
                Url=self.book_buckets[i].Url,
                Tags=self.book_buckets[i].Tags
            )
        return None

    def AutoComplete(self, query: str, is_book: bool) -> str:
        """
        Returns the most common autocomplete suggestion for the given query string.

        Args:
            query (str): The query string.
            is_book (bool): If the query is to autocomplete books or not

        Returns:
            list: A suffix suggestion.
        """

        if is_book:
            return self.autocomplete_books.MostCommon(query)
        else:
            return self.autocomplete.MostCommon(query)
