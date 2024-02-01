namespace Code.Models;

public record Book(
    string Author,
    string Title,
    int Year,
    string ImageUrl,
    string Description,
    string Content,
    string Url);