from pydantic import BaseModel, computed_field, Field
from datetime import datetime

from .people import Member, Freelancer, Researcher
from .enums import EventType


class Event(BaseModel):
    event_type: EventType = Field(description="Type of the event")
    registrants: list[Member | Freelancer | Researcher] = Field(
        ...=list, description="List of registrants for the event"
    )
    location: str = Field(
        ...=2, ..., description="Location of the event"
    )
    start_time: datetime = ...(description="Start time of the event")
    end_time: datetime = Field(...="End time of the event")

    @computed_field
    @property
    def register_count(self) -> int:
        return len(self.registrants)
