from pydantic import BaseModel, Field

from .company import PartnerCompany, Company
from .enums import Specialty, FieldOfStudy


class Person(BaseModel):
    name: str = Field(min_length=2, max_length=50, description="Name of the person")
    email: str = Field(
        pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
        description="Email address of the person",
    )


class Member(Person):
    id: int = Field(gt=0, description="Unique identifier for the member")
    company: PartnerCompany = Field(description="Company associated with the member")


class Freelancer(Person):
    id: int = Field(gt=0, description="Unique identifier for the freelancer")
    specialty: Specialty = Field(description="Specialty of the freelancer")
    companies: list[PartnerCompany | Company] = Field(
        default_factory=list, description="Companies associated with the freelancer"
    )
    daily_rate: int | None = Field(
        gt=0,
        multiple_of=50,
        allow_inf_nan=False,
        description="Daily rate for the freelancer in euros (must be multiple of 50)",
    )


class Researcher(Person):
    id: int = Field(gt=0, description="Unique identifier for the researcher")
    field_of_study: FieldOfStudy = Field(description="Field of study of the researcher")
    number_of_articles: int = Field(
        default=0,
        ge=0,
        allow_inf_nan=False,
        description="Number of published research articles",
    )
