namespace Gui.Events;

public interface IEventService
{
    // Query search
    public event Action<string> OnQuerySearch;
    public void TriggerOnQuerySearch(string query);
}