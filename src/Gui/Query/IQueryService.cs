using Gui.Models;

namespace Gui.Query;

public interface IQueryService
{
    Task<QueryResult> QueryAsync(string query, string previouslyRead = "", int pageNumber = 1);
    Task<string> AutoCompleteAsync(string query); 
    Task<string> AutoCompleteBookAsync(string query); 
}