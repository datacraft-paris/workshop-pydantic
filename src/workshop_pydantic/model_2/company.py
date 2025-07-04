from pydantic import BaseModel, HttpUrl

from .enums import Sector


class Company(BaseModel):
    name: str
    sector: ...
    website: HttpUrl | None
    employee_count: int


class PartnerCompany(Company):
    is_active: bool
