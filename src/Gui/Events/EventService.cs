namespace Gui.Events;

public class EventService : IEventService
{
    public event Func<(string, string, int), Task> OnQuerySearch = null!;

    public void TriggerOnQuerySearch((string, string, int) query)
    {
        OnQuerySearch?.Invoke(query);
    }
}