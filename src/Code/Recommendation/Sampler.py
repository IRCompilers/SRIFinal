from random import randint
from typing import List

from src.Code.Models import BookEntry


def CreateSampleBooks() -> List[BookEntry]:
    books = [
        BookEntry.BookEntry(
            Title="The Great Gatsby",
            Author="F. Scott Fitzgerald",
            Year=1925,
            Description="The Great Gatsby is a novel by American author F. Scott Fitzgerald. The story takes place in 1922, during the Roaring Twenties, a time of prosperity in the United States after World War I. The book received critical acclaim and is generally considered Fitzgerald's best work. It is also widely regarded as a Great American Novel and a literary classic, capturing the essence of an era.",
            Text="The Great Gatsby is a novel by American author F. Scott Fitzgerald. The story takes place in 1922, during the Roaring Twenties, a time of prosperity in the United States after World War I. The book received critical acclaim and is generally considered Fitzgerald's best work. It is also widely regarded as a Great American Novel and a literary classic, capturing the essence of an era.",
            ImageUrl="https://upload.wikimedia.org/wikipedia/commons/4/4f/To_Kill_a_Mockingbird_%28first_edition_cover%29.jpg",
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
        ),
        BookEntry.BookEntry(
            Title="1984",
            Author="George Orwell",
            Year=1949,
            Description="1984 is a dystopian social science fiction novel by English novelist George Orwell. It was published on 8 June 1949 by Secker & Warburg as Orwell's ninth and final book completed in his lifetime. Thematically, 1984 centres on the consequences of totalitarianism, mass surveillance, and repressive regimentation of persons and behaviours within society.",
            Text="1984 is a dystopian social science fiction novel by English novelist George Orwell. It was published on 8 June 1949 by Secker & Warburg as Orwell's ninth and final book completed in his lifetime. Thematically, 1984 centres on the consequences of totalitarianism, mass surveillance, and repressive regimentation of persons and behaviours within society.",
            ImageUrl="https://upload.wikimedia.org/wikipedia/commons/4/4f/To_Kill_a_Mockingbird_%28first_edition_cover%29.jpg",
            Url="https://en.wikipedia.org/wiki/Nineteen_Eighty-Four"
        ),
        BookEntry.BookEntry(
            Title="The Catcher in the Rye",
            Author="J. D. Salinger",
            Year=1951,
            Description="The Catcher in the Rye is a novel by J. D. Salinger, partially published in serial form in 1945–1946 and as a novel in 1951. It was originally intended for adults, but is often read by adolescents for its themes of angst and alienation, and as a critique on superficiality in society.",
            Text="The Catcher in the Rye is a novel by J. D. Salinger, partially published in serial form in 1945–1946 and as a novel in 1951. It was originally intended for adults, but is often read by adolescents for its themes of angst and alienation, and as a critique on superficiality in society.",
            ImageUrl="https://upload.wikimedia.org/wikipedia/commons/4/4f/To_Kill_a_Mockingbird_%28first_edition_cover%29.jpg",
            Url="https://en.wikipedia.org/wiki/The_Catcher_in_the_Rye"
        ),
        BookEntry.BookEntry(
            Title="The Grapes of Wrath",
            Author="John Steinbeck",
            Year=1939,
            Description="The Grapes of Wrath is an American realist novel written by John Steinbeck and published in 1939. The book won the National Book Award and Pulitzer Prize for fiction, and it was cited prominently when Steinbeck was awarded the Nobel Prize in 1962.",
            Text="The Grapes of Wrath is an American realist novel written by John Steinbeck and published in 1939. The book won the National Book Award and Pulitzer Prize for fiction, and it was cited prominently when Steinbeck was awarded the Nobel Prize in 1962.",
            ImageUrl="https://upload.wikimedia.org/wikipedia/commons/4/4f/To_Kill_a_Mockingbird_%28first_edition_cover%29.jpg",
            Url="https://en.wikipedia.org/wiki/The_Grapes_of_Wrath"
        ),
        BookEntry.BookEntry(
            Title="The Sun Also Rises",
            Author="Ernest Hemingway",
            Year=1926,
            Description="The Sun Also Rises is a 1926 novel by American writer Ernest Hemingway that portrays American and British expatriates who travel from Paris to the Festival of San Fermín in Pamplona to watch the running of the bulls and the bullfights.",
            Text="The Sun Also Rises is a 1926 novel by American writer Ernest Hemingway that portrays American and British expatriates who travel from Paris to the Festival of San Fermín in Pamplona to watch the running of the bulls and the bullfights.",
            ImageUrl="https://upload.wikimedia.org/wikipedia/commons/4/4f/To_Kill_a_Mockingbird_%28first_edition_cover%29.jpg",
            Url="https://en.wikipedia.org/wiki/The_Sun_Also_Rises"
        ),
    ]

    return books


def get_hardcoded_book_descriptions():
    """Returns a list of 20 hardcoded book descriptions."""

    book_descriptions = [
        "A young wizard named Harry Potter discovers his magical heritage and begins his training at Hogwarts School of Witchcraft and Wizardry.",
        "A dystopian novel about a totalitarian society where books are banned and independent thinking is suppressed.",
        "A classic science fiction novel about a group of astronauts who travel through a wormhole to a distant galaxy.",
        "A coming-of-age story about a young girl's life in the American South during the Great Depression.",
        "A psychological thriller about a wealthy New York socialite who suspects her husband is trying to kill her.",
        "A mystery novel about a detective who is hired to solve the crime surrounding a wealthy family's fortune.",
        "A historical fiction novel about the lives of four sisters growing up in New England during the Civil War.",
        "A fantasy novel about a young warrior exiled from his country willing to do anything to be accepted again. ",
        "A science fiction novel about a group of astronauts who are stranded on a distant planet after their ship crashes.",
        "A dystopian novel about a society where people are divided into factions based on their personalities.",
    ]

    return book_descriptions

def get_hardcoded_book_tags():
    """Returns a list of lists of hardcoded book tags."""

    book_tags = [
        ["fantasy", "magic", "wizardry", "school", "coming-of-age"],
        ["dystopia", "censorship", "totalitarianism", "freedom", "rebellion"],
        ["science fiction", "space travel", "aliens", "wormholes", "time travel"],
        ["historical fiction", "Great Depression", "American South", "racism", "poverty"],
        ["thriller", "mystery", "murder", "suspense", "psychological"],
        ["mystery", "police", "suspense", "fiction"],
        ["historical", "England", "Civil War", "family", "drama"],
        ["fantasy", "swordsmanship", "freedom", "epic", "adolescents"],
        ["science fiction", "space travel", "survival", "crash"],
        ["dystopia", "factions", "segregation", "totalitarianism"]
    ]

    return book_tags
