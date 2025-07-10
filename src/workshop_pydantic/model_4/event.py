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

    @model_validator(mode=...)
    @classmethod
    def check_event_data(cls, data):
        if "start_time" in data and ... in ...:
            if data["start_time"] ... data[...]:
                raise ValueError("Start time must be before end time")
        return ...

    @model_validator(mode="after")
    def check_event_registration_and_speakers(...):
        if self.event_type == ... and len(self.registrants) < ...:
            raise ...(
                "Datathon events must have at least 10 registered attendees"
            )
        if not self.registrants and ... != EventType.CONFERENCE:
            raise ValueError("Non-conference events must have at least one registrant")
        return self
