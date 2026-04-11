from api.auth import get_calendar_service
from api.calendar_client import get_upcoming_events
from api.parser import parse_google_event

# Can pass timeframe to run_scheduler in the future that then gets passed to raw_events
# def run_scheduler():
#     # 1. Authenticate
#     service = get_calendar_service()

#     # 2. Fetch Raw Event Data
#     print("Connecting to Google...")
#     raw_events = get_upcoming_events(service, days=7)

#     # 3. Parse Data
#     print (f"Parsing {len(raw_events)} events...")
#     parsed_events = [parse_google_event(e) for e in raw_events]

#     # 4. Next Phase: scoring_logic 

#     print("\n--- Schedule ---")
#     for event in parsed_events:
#         status = "Organizer" if event.is_organizer else "Guest"
#         date_str = event.start.strftime('%b %d')
#         start_str = event.start.strftime('%H:%M')
#         end_str = event.end.strftime('%H:%M')
#         print(f"[{date_str} | {start_str} - {end_str}] {event.title} ({status})")

def run_multi_user_test():

    users = ["test_user_A", "test_user_B"]
    services = {}

    for userId in users:
        print(f"--- Setting up session for: {userId} ---")
        services[userId] = get_calendar_service(user_id=userId, force_login=False)
    
    # Fetch data for both
    events_a = [parse_google_event(e) for e in get_upcoming_events(services[users[0]])]
    events_b = [parse_google_event(e) for e in get_upcoming_events(services[users[1]])]
    
    print(f"User A has {len(events_a)} events.")
    print(f"User B has {len(events_b)} events.")

    print("\n--- User A Schedule ---")
    for event in events_a:
        status = "Organizer" if event.is_organizer else "Guest"
        date_str = event.start.strftime('%b %d')
        start_str = event.start.strftime('%H:%M')
        end_str = event.end.strftime('%H:%M')
        print(f"[{date_str} | {start_str} - {end_str}] {event.title} ({status})")

    print("\n--- User B Schedule ---")
    for event in events_b:
        status = "Organizer" if event.is_organizer else "Guest"
        date_str = event.start.strftime('%b %d')
        start_str = event.start.strftime('%H:%M')
        end_str = event.end.strftime('%H:%M')
        print(f"[{date_str} | {start_str} - {end_str}] {event.title} ({status})")

if __name__ == "__main__":
    run_multi_user_test()
