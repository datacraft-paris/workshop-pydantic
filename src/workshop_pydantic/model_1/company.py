from pydantic import BaseModel, HttpUrl


class Company(BaseModel):
    name: str
    sector: str
    website: HttpUrl | ...
    employee_count: ...


class PartnerCompany(...):
    is_active: bool
