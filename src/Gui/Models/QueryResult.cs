namespace Gui.Models;

public record QueryResult(
    int Total,
    BookCard[] Results);