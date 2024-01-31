using Code.Models;

namespace Code;

public static class Query
{
    public static IEnumerable<BookCard> GetRecommendations(string query)
    {
        return new List<BookCard>
        {
            new(
                "The Fellowship of the Ring",
                "J.R.R. Tolkien",
                1954,
                4.34f,
                "demo.jpeg",
                "The first part of the epic Lord of the Rings trilogy.",
                ["Fantasy", "Adventure"],
                "https://www.goodreads.com/book/show/34.The_Fellowship_of_the_Ring"
            ),
            new(
                "The Two Towers",
                "J.R.R. Tolkien",
                1954,
                4.24f,
                "demo.jpeg",
                "The second part of the epic Lord of the Rings trilogy.",
                ["Fantasy", "Adventure"],
                "https://www.goodreads.com/book/show/34.The_Fellowship_of_the_Ring"
            ),
            new(
                "The Return of the King",
                "J.R.R. Tolkien",
                1955,
                4.52f,
                "demo.jpeg",
                "The third part of the epic Lord of the Rings trilogy.",
                new[] { "Fantasy", "Adventure" },
                "https://www.goodreads.com/book/show/34.The_Fellowship_of_the_Ring"
            ),
            new(
                "The Hobbit",
                "J.R.R. Tolkien",
                1937,
                4.26f,
                "demo.jpeg",
                "The prequel to the epic Lord of the Rings trilogy.",
                ["Fantasy", "Adventure"],
                "https://www.goodreads.com/book/show/34.The_Fellowship_of_the_Ring"
            ),
            new(
                "The Silmarillion",
                "J.R.R. Tolkien",
                1977,
                3.9f,
                "demo.jpeg",
                "The history of the First Age of Middle-earth.",
                ["Fantasy", "Adventure"],
                "https://www.goodreads.com/book/show/34.The_Fellowship_of_the_Ring")
        };
    }
}