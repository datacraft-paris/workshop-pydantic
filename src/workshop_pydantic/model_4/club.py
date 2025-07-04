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

    ...

    ...
