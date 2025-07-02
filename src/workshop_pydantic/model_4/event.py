from pydantic import BaseModel, computed_field, Field, model_validator
from datetime import datetime

from .people import Member, Freelancer, Researcher
from .enums import EventType


class Event(BaseModel):
    event_type: EventType = Field(description="Type of the event")
    registrants: list[Member | Freelancer | Researcher] = Field(
        default_factory=list, description="List of registrants for the event"
    )
    location: str = Field(
        min_length=2, max_length=200, description="Location of the event"
    )
    start_time: datetime = Field(description="Start time of the event")
    end_time: datetime = Field(description="End time of the event")

    @computed_field
    @property
    def register_count(self) -> int:
        return len(self.registrants)

    @model_validator(mode="before")
    @classmethod
    def check_event_data(cls, data):
        if "start_time" in data and "end_time" in data:
            if data["start_time"] >= data["end_time"]:
                raise ValueError("Start time must be before end time")
        return data

    @model_validator(mode="after")
    def check_event_registration_and_speakers(self):
        if self.event_type == EventType.DATATHON and len(self.registrants) < 10:
            raise ValueError(
                "Datathon events must have at least 10 registered attendees"
            )
        if not self.registrants and self.event_type != EventType.NETWORKING:
            raise ValueError("Non-networking events must have at least one registrant")
        return self
