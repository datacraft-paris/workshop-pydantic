from pydantic import BaseModel

from .enums import Sector


class Company(BaseModel):
    name: str
    sector: Sector
    website: str | None
    employee_count: int


class PartnerCompany(Company):
    is_active: bool
