from pydantic import BaseModel

from .company import PartnerCompany


class Club(BaseModel):
    members: ...
    partner_companies: list[PartnerCompany]
    events: ...
