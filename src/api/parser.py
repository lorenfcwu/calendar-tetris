from engine.models import CalendarEvent, Attendee
from datetime import datetime

def parse_google_event(raw_event: dict) -> CalendarEvent:
    """Converts a single Google Calendar API resource into a CalendarEvent object."""


    # 1. Handles Time Logic
    start_info = raw_event['start']
    is_all_day = 'date' in start_info

    if is_all_day:
        start = datetime.strptime(start_info['date'], '%Y-%m-%d')
        end = datetime.strptime(raw_event['end']['date'], '%Y-%m-%d')
    else:
        start = datetime.fromisoformat(start_info['dateTime'].replace('Z', '+00:00'))
        end = datetime.fromisoformat(raw_event['end']['dateTime'].replace('Z', '+00:00'))

    # 2. Handles Attendees
    raw_attendees = raw_event.get('attendees', [])
    attendees_list = []
    for a in raw_attendees:
        attendees_list.append(Attendee(
            email=a.get('email', 'unknown'),
            status=a.get('responseStatus', 'needsAction'),
            is_optional=a.get('optional', False)
        ))

    # 3. Instantiate Model
    return CalendarEvent(
        event_id=raw_event['id'],
        title=raw_event.get('summary', "No Title"),
        start=start,
        end=end,
        is_organizer=raw_event.get('organizer', {}).get('self', False),
        is_all_day=is_all_day,
        original_json=raw_event,
        attendees=attendees_list
    )