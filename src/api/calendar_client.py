from datetime import datetime, timedelta, timezone
from api.auth import get_calendar_service

def get_upcoming_events(service, days=7):
    # Create an 'aware' UTC datetime
    now = datetime.now(timezone.utc)
    then = now + timedelta(days=days)
    
    # Google API expects RFC3339 format (e.g., '2026-04-09T10:00:00Z')
    # isoformat() on an aware object adds '+00:00'; we swap it for 'Z'
    time_min = now.isoformat().replace('+00:00', 'Z')
    time_max = then.isoformat().replace('+00:00', 'Z')

    print(f"Fetching events for the next {days} days...")
    
    events_result = service.events().list(
        calendarId='primary', 
        timeMin=time_min,
        timeMax=time_max,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    
    return events_result.get('items', [])

if __name__ == '__main__':
    service = get_calendar_service()
    events = get_upcoming_events(service)

    if not events:
        print('No upcoming events found.')
    else:
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(f"- {start}: {event.get('summary', 'No Title')}")
            print(event) 