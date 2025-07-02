from pydantic import BaseModel, HttpUrl

from .enums import Sector


class Company(BaseModel):
    name: str
    website: HttpUrl | None
    sector: Sector
    employee_count: int


class PartnerCompany(Company):
    is_active: bool
