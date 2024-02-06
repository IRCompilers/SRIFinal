namespace Gui.Models;

public record BookCard(
    string Author,
    string Title,
    string Description,
    float Rating,
    string ImageUrl,
    string Url,
    string[] Tags
    );