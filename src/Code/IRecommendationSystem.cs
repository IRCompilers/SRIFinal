using Code.Models;

namespace Code;

public interface IRecommendationSystem
{
    Task<IEnumerable<BookCard>> GetRecommendations(string query);
    Task AddBooks(IEnumerable<Book> book);
    Task UpdateFromFolder();
}