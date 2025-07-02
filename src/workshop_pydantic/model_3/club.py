from pydantic import BaseModel, Field

from .people import Member, Freelancer, Researcher
from .company import PartnerCompany
from .event import Event


class Club(BaseModel):
    name: str = Field(min_length=2, max_length=100, description="Name of the club")
    members: list[Member | Freelancer | Researcher] = Field(
        default_factory=list, description="List of club members"
    )
    partner_companies: list[PartnerCompany] = Field(
        default_factory=list, description="List of partner companies"
    )
    events: list[Event] = Field(
        default_factory=list, description="List of events organized by the club"
    )
