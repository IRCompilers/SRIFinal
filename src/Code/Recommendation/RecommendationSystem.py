# Python imports
from concurrent.futures import ThreadPoolExecutor
from typing import List

# External imports
from gensim import similarities, corpora

# Internal imports
from src.Code.Models import BookEntry
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

        ...

        Attributes
        ----------
        dictionary : corpora.Dictionary
            a dictionary that maps each word to its "id"
        book_buckets : list
            a list of book buckets
        autocomplete : Trie
            a Trie data structure for autocomplete functionality

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
        self.LoadResources()

    @staticmethod
    def AddBooks(books: List[BookEntry]):
        """
            Adds books to the system.

            Args:
                books (List[BookEntry]): The list of books to add.
        """
        texts = [book.Text for book in books]
        preprocessed_documents = Preprocess(texts)
        trie = Trie()

        for word in flatten_list(preprocessed_documents):
            trie.Insert(word)

        SaveTrieToJson(trie, "Resources/autocomplete_trie.json")

        tags = BookRecommendationSystem.PredictTagsInParallel(preprocessed_documents)
        vectorized_documents, dictionary = Vectorize(preprocessed_documents)
        SaveBooksToJson(books, vectorized_documents, tags, 'Resources/books.json')
        dictionary.save('Resources/dictionary.pkl')

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
        except FileNotFoundError:
            print("Error loading resources - Files where not found. Please add books to the system first.")

    def Query(self, query: str) -> List[BookCard]:
        """
        Queries the system with the given query string. Uses matrix cosine similarity to find the most similar books.

        Args:
            query (str): The query string.

        Returns:
            List[BookCard]: A list of book cards that match the query string.
        """
        preprocessed_query = Preprocess([query])
        query_vector, _ = Vectorize(preprocessed_query, self.dictionary, True)

        index = similarities.MatrixSimilarity([bucket.Vector for bucket in self.book_buckets])
        sims = index[query_vector]

        with ThreadPoolExecutor() as executor:
            book_cards = list(executor.map(self.CreateBookCard, enumerate(sims[0])))

        book_cards = [book_card for book_card in book_cards if book_card is not None]

        book_cards = sorted(book_cards, key=lambda x: x.Rating, reverse=True)

        return book_cards

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
                Tags=[]
            )
        return None

    def AutoComplete(self, query: str) -> str:
        """
        Returns the most common autocomplete suggestion for the given query string.

        Args:
            query (str): The query string.

        Returns:
            list: A suffix suggestion.
        """
        return self.autocomplete.MostCommon(query)
