namespace Gui.Models;

public record BookCard(
    string Author,
    string Title,
    string Description,
    int Year,
    float Rating,
    string ImageUrl,
    string Url,
    string[] Tags
    );