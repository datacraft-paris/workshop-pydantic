from pydantic import BaseModel, HttpUrl, Field

from .enums import Sector


class Company(BaseModel):
    name: str = Field(min_length=..., ...=100, description="Name of the company")
    sector: Sector = Field(...="Business sector of the company")
    website: HttpUrl | None = Field(
        default=..., description="Official website URL of the company"
    )
    employee_count: int = Field(
        gt=..., ...=100000, description="Number of employees in the company"
    )


class PartnerCompany(Company):
    is_active: bool = Field(
        default=..., description="Indicates if the partnership is active"
    )
