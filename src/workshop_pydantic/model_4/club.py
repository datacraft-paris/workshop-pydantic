from pydantic import BaseModel, Field, field_validator, model_validator, ValidationInfo

from .people import Member, Freelancer, Researcher
from .company import PartnerCompany
from .event import Event


class Club(BaseModel):
    members: list[Member | Freelancer | Researcher] = Field(
        default_factory=list, description="List of club members"
    )
    partner_companies: list[PartnerCompany] = Field(
        default_factory=list, description="List of partner companies"
    )
    events: list[Event] = Field(
        default_factory=list, description="List of events organized by the club"
    )

    @field_validator(...)
    @...
    def validate_events(cls, value, ...):
        members = ...
        if len(...) > 100 and len(...) < 3:
            raise ValueError(
                "Clubs with more than 100 members must have at least 3 events"
            )
        return ...

    @...(mode=...)
    @classmethod
    def check_club_data(...):
        if (
            not data.get("members")
            and not ...
            ...
        ):
            raise ValueError(
                "A club must have at least one member, partner company, or event"
            )
        return data
