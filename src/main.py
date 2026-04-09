from api.auth import get_calendar_service
from api.calendar_client import get_upcoming_events
from api.parser import parse_google_event

# Can pass timeframe to run_scheduler in the future that then gets passed to raw_events
def run_scheduler():
    # 1. Authenticate
    service = get_calendar_service()

    # 2. Fetch Raw Event Data
    print("Connecting to Google...")
    raw_events = get_upcoming_events(service, days=7)

    # 3. Parse Data
    print (f"Parsing {len(raw_events)} events...")
    parsed_events = [parse_google_event(e) for e in raw_events]

    # 4. Next Phase: scoring_logic 

    print("\n--- Schedule ---")
    for event in parsed_events:
        status = "Organizer" if event.is_organizer else "Guest"
        date_str = event.start.strftime('%b %d')
        start_str = event.start.strftime('%H:%M')
        end_str = event.end.strftime('%H:%M')
        print(f"[{date_str} | {start_str} - {end_str}] {event.title} ({status})")


if __name__ == "__main__":
    run_scheduler()