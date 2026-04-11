from engine.models import CalendarEvent

def calculate_score(event: CalendarEvent):
    score = 10.0

    if event.is_all_day:
        return 1000.0

    # length of event
    event_len = event.end - event.start
    duration_hours = event_len.total_seconds / 3600
    score *= duration_hours

    # number of attendees
    score += event.accepted_count ** 2
    score += (event.attendees_count - event.accepted_count)

    # whether they organized it or not
    if not event.is_organizer:
        score *= 1.5

    return score
