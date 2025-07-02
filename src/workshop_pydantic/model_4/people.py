from pydantic import BaseModel, Field, field_validator, ValidationInfo

from .company import PartnerCompany, Company
from .enums import Specialty, FieldOfStudy


class Person(BaseModel):
    name: str = Field(min_length=2, max_length=50, description="Name of the person")
    email: str = Field(
        regex=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
        description="Email address of the person",
    )

    @field_validator("name")
    @classmethod
    def name_must_not_contain_special_chars(cls, value):
        if not value.isalpha():
            raise ValueError("Name must not contain special characters or numbers")
        return value


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

    @field_validator("daily_rate")
    @classmethod
    def validate_daily_rate(cls, value, info: ValidationInfo):
        if value is not None:
            specialty = info.data.get("specialty")
            if specialty == Specialty.SOFTWARE_DEVELOPMENT and value < 300:
                raise ValueError(
                    "Daily rate for Software Development must be at least 300 euros"
                )
            if specialty == Specialty.DATA_SCIENCE and value < 350:
                raise ValueError(
                    "Daily rate for Data Science must be at least 350 euros"
                )
            if specialty == Specialty.CYBERSECURITY and value < 400:
                raise ValueError(
                    "Daily rate for Cybersecurity must be at least 400 euros"
                )
            if specialty == Specialty.DEVOPS and value < 375:
                raise ValueError("Daily rate for DevOps must be at least 375 euros")
        return value


class Researcher(Person):
    id: int = Field(gt=0, description="Unique identifier for the researcher")
    field_of_study: FieldOfStudy = Field(description="Field of study of the researcher")
    number_of_articles: int = Field(
        default=0,
        ge=0,
        allow_inf_nan=False,
        description="Number of published research articles",
    )
