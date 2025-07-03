from pydantic import BaseModel, HttpUrl


class Company(BaseModel):
    name: str
    sector: str
    website: HttpUrl | None
    employee_count: int


class PartnerCompany(Company):
    is_active: bool
