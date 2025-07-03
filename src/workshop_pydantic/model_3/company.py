from pydantic import BaseModel, HttpUrl, Field

from .enums import Sector


class Company(BaseModel):
    name: str = Field(...=2, max_length=..., description="Name of the company")
    sector: Sector = Field(description="Business sector of the company")
    website: HttpUrl | None = Field(
        default=..., description="Official website URL of the company"
    )
    employee_count: int = ...

class PartnerCompany(Company):
    is_active: bool = ...
