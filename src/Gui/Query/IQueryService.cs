using Gui.Models;

namespace Gui.Query;

public interface IQueryService
{
    Task<BookCard[]> QueryAsync(string query, string previouslyRead = "");
    Task<string> AutoCompleteAsync(string query); 
    Task<string> AutoCompleteBookAsync(string query); 
}