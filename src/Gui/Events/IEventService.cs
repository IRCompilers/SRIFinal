namespace Gui.Events;

public interface IEventService
{
    // Query search
    public event Func<(string query, string read, int pageNumber), Task> OnQuerySearch;
    public void TriggerOnQuerySearch((string, string, int) query);
}