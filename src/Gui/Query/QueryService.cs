using Gui.Models;

namespace Gui.Query;

public class QueryService(IHttpClientFactory httpClientFactory, IConfiguration configuration)
    : IQueryService
{
    private readonly HttpClient _httpClient = httpClientFactory.CreateClient();
    private readonly string _baseAddress = configuration.GetSection("ApiSettings:BaseAddress").Value ?? throw new InvalidOperationException("BaseAddress not provided in appsettings.json");

    public async Task<BookCard[]> QueryAsync(string query, string previouslyRead = "")
    {
        var url = $"{_baseAddress}/query?query={query}";
        
        if(previouslyRead != "")
            url += $"&previouslyRead={previouslyRead}";
        
        var response = await _httpClient.GetAsync(url);
        response.EnsureSuccessStatusCode();
        return await response.Content.ReadFromJsonAsync<BookCard[]>() ?? throw new InvalidOperationException("Response was not in the correct format.");
    }
    
    public async Task<string> AutoCompleteAsync(string query)
    {
        var response = await _httpClient.GetAsync($"{_baseAddress}/autocomplete?query={query}");
        return await response.Content.ReadAsStringAsync();
    }

    public async Task<string> AutoCompleteBookAsync(string query)
    {
        var response = await _httpClient.GetAsync($"{_baseAddress}/autocomplete?query={query}&is_book=true");
        return await response.Content.ReadAsStringAsync();
    }
}