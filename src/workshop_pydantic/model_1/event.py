from pydantic import BaseModel, computed_field
from datetime import datetime

from .people import Member, Freelancer, Researcher


class Event(BaseModel):
    name: str
    event_type: str
    registrants: list[Member | Freelancer | Researcher]
    location: str
    start_time: datetime
    end_time: datetime

    @computed_field
    @property
    def register_count(self) -> int:
        return len(self.registrants)
