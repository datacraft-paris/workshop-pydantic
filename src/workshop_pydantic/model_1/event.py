from pydantic import BaseModel, computed_field
from datetime import datetime

from .people import Member, Freelancer, Researcher


class Event(BaseModel):
    name: ...
    event_type: str
    registrants: list[Member | ... | Researcher]
    location: str
    start_time: datetime
    end_time: ...

    @...
    @property
    def register_count(self) -> ... :
        return len(self....)
