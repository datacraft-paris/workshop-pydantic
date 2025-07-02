from pydantic import BaseModel, HttpUrl


class Company(BaseModel):
    name: str
    website: HttpUrl | None
    sector: str
    employee_count: int


class PartnerCompany(Company):
    is_active: bool
