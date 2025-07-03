from pydantic import BaseModel, HttpUrl, Field, field_validator, ValidationInfo

from .enums import Sector


class Company(BaseModel):
    name: str = Field(min_length=2, max_length=100, description="Name of the company")
    sector: Sector = Field(description="Business sector of the company")
    website: HttpUrl | None = Field(
        default=None, description="Official website URL of the company"
    )
    employee_count: int = Field(
        gt=0, lt=100000, description="Number of employees in the company"
    )

    @...("website")
    @classmethod
    def website_required_for_finance(..., value, ...: ValidationInfo):
        sector = info.data.get(...)
        if ... == Sector.FINANCE and ... is None:
            raise ValueError("Finance companies must have a website")
        return value


class PartnerCompany(Company):
    is_active: bool = Field(
        default=True, description="Indicates if the partnership is active"
    )
