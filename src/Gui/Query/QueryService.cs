using Gui.Models;

namespace Gui.Query;

public class QueryService(IHttpClientFactory httpClientFactory, IConfiguration configuration)
    : IQueryService
{
    private readonly HttpClient _httpClient = httpClientFactory.CreateClient();
    private readonly string _baseAddress = configuration.GetSection("ApiSettings:BaseAddress").Value ?? throw new InvalidOperationException("BaseAddress not provided in appsettings.json");

    public async Task<BookCard[]> QueryAsync(string query)
    {
        var response = await _httpClient.GetAsync($"{_baseAddress}/query?query={query}");
        response.EnsureSuccessStatusCode();
        return await response.Content.ReadFromJsonAsync<BookCard[]>() ?? throw new InvalidOperationException("Response was not in the correct format.");
    }
}