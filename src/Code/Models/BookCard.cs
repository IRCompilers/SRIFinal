namespace Code.Models;

public record BookCard(
    string Title,
    string Author,
    int Year,
    float Rating,
    string ImageUrl,
    string Description,
    string[] Tags,
    string Url
);