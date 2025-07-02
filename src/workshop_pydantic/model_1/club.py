from pydantic import BaseModel

from .people import Member, Freelancer, Researcher
from .company import PartnerCompany
from .event import Event


class Club(BaseModel):
    members: ...
    partner_companies: list[PartnerCompany]
    events: ...
