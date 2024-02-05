namespace Gui.Events;

public class EventService : IEventService
{
    public event Func<(string, string), Task> OnQuerySearch = null!;

    public void TriggerOnQuerySearch((string, string) query)
    {
        OnQuerySearch?.Invoke(query);
    }
}