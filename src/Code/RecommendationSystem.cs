using Code.Models;

namespace Code;

public class RecommendationSystem: IRecommendationSystem
{
    public Task<IEnumerable<BookCard>> GetRecommendations(string query)
    {
        // Create a sample list of books
        return Task.FromResult<IEnumerable<BookCard>>(new List<BookCard>
        {
            new("Author1", "Title1", 2021, 4.5f, "demo.jpeg", "Description1", ["Fantasy", "Spectre"], "https://example.com/url1"),
            new("Author2", "Title2", 2022, 4.5f, "demo.jpeg", "Description2", ["Fantasy", "Spectre"], "https://example.com/url2"),
            new("Author3", "Title3", 2023, 4.5f, "demo.jpeg", "Description3", ["Fantasy", "Spectre"], "https://example.com/url3"),
            new("Author4", "Title4", 2023, 4.5f, "demo.jpeg", "Description4", ["Fantasy", "Spectre"], "https://example.com/url3"),
            new("Author5", "Title5", 2023, 4.5f, "demo.jpeg", "Description5", ["Fantasy", "Spectre"], "https://example.com/url3"),
            new("Author6", "Title6", 2023, 4.5f, "demo.jpeg", "Description6", ["Fantasy", "Spectre"], "https://example.com/url3"),
        });
    }

    public Task AddBooks(IEnumerable<Book> book)
    {
        throw new NotImplementedException();
    }

    public Task UpdateFromFolder()
    {
        throw new NotImplementedException();
    }
}