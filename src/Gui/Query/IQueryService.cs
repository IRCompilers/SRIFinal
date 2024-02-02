using Gui.Models;

namespace Gui.Query;

public interface IQueryService
{
    Task<BookCard[]> QueryAsync(string query);
}