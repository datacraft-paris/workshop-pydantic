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

    @field_validator("events")
    @classmethod
    def validate_events(cls, value, info: ValidationInfo):
        members = info.data.get("members", [])
        if len(members) > 100 and len(value) < 3:
            raise ValueError(
                "Clubs with more than 100 members must have at least 3 events"
            )
        return value

    @model_validator(mode="before")
    @classmethod
    def check_club_data(cls, data):
        if (
            not data.get("members")
            and not data.get("partner_companies")
            and not data.get("events")
        ):
            raise ValueError(
                "A club must have at least one member, partner company, or event"
            )
        return data
