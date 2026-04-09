from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

@dataclass(frozen=True)
class Attendee:
    email: str
    # Google API statuses: 'needsAction', 'declined', 'tentative', 'accepted'
    status: str
    is_optional: bool = False

@dataclass(frozen=True)
class CalendarEvent:
    event_id: str
    title: str
    start: datetime
    end: datetime
    attendees: List[Attendee] = field(default_factory=list)
    is_organizer: bool
    is_all_day: bool
    original_json: dict
    disruption_score: float = 0.0

    @property
    def attendees_count(self) -> int:
        return len(self.attendees)
    
    @property
    def accepted_count(self) -> int:
        return len([a for a in self.attendees if a.status == 'accepted'])
