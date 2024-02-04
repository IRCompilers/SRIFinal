namespace Gui.Events;

public class EventService : IEventService
{
    public event Action<string> OnQuerySearch = null!;

    public void TriggerOnQuerySearch(string query)
    {
        OnQuerySearch?.Invoke(query);
    }
}