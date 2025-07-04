from pydantic import BaseModel, computed_field, Field
from datetime import datetime

from .people import Member, Freelancer, Researcher
from .enums import EventType


class Event(BaseModel):
    event_type: EventType = ...
    registrants: list[Member | Freelancer | Researcher] = ...
    location: str = ...
    start_time: datetime = ...
    end_time: datetime = ...

    @computed_field
    @property
    def register_count(self) -> int:
        return len(self.registrants)
