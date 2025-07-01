from pydantic import BaseModel, Field, HttpUrl, computed_field
from datetime import datetime
from enum import Enum


class Sector(str, Enum):
    TECHNOLOGY = "Technology"
    HEALTHCARE = "Healthcare"
    EDUCATION = "Education"
    FINANCE = "Finance"


class Specialty(str, Enum):
    SOFTWARE_DEVELOPMENT = "Software Development"
    DATA_SCIENCE = "Data Science"
    CYBERSECURITY = "Cybersecurity"
    DEVOPS = "DevOps"


class FieldOfStudy(str, Enum):
    COMPUTER_SCIENCE = "Computer Science"
    BIOLOGY = "Biology"
    PHYSICS = "Physics"
    CHEMISTRY = "Chemistry"


class EventType(str, Enum):
    WORKSHOP = "Workshop"
    CONFERENCE = "Conference"
    SEMINAR = "Seminar"
    DATATHON = "Datathon"


class Person(BaseModel):
    name: str = Field(min_length=2, max_length=50, description="Name of the person")
    email: str = Field(
        regex=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
        description="Email address of the person",
    )


class Company(BaseModel):
    name: str = Field(min_length=2, max_length=100, description="Name of the company")
    website: HttpUrl | None = Field(
        default=None, description="Official website URL of the company"
    )
    sector: Sector = Field(description="Business sector of the company")
    employee_count: int = Field(
        gt=0, lt=100000, description="Number of employees in the company"
    )


class PartnerCompany(Company):
    is_active: bool = Field(
        default=True, description="Indicates if the partnership is active"
    )


class Member(Person):
    id: int = Field(gt=0, description="Unique identifier for the member")
    company: PartnerCompany = Field(description="Company associated with the member")


class Freelancer(Person):
    id: int = Field(gt=0, description="Unique identifier for the freelancer")
    specialty: Specialty = Field(description="Specialty of the freelancer")
    company: list[PartnerCompany | Company] = Field(
        default_factory=None, description="Companies associated with the freelancer"
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
    company: list[PartnerCompany | Company] = Field(
        default_factory=None, description="Companies associated with the researcher"
    )
    number_of_articles: int = Field(
        default=0,
        ge=0,
        allow_inf_nan=False,
        description="Number of published research articles",
    )


class Event(BaseModel):
    name: str = Field(min_length=2, max_length=100, description="Name of the event")
    event_type: EventType = Field(description="Type of the event")
    registrants: list[Member | Freelancer | Researcher] = Field(
        default_factory=list, description="List of registrants for the event"
    )
    location: str = Field(
        min_length=2, max_length=200, description="Location of the event"
    )
    start_time: datetime = Field(description="Start time of the event")
    end_time: datetime = Field(description="End time of the event")

    @computed_field
    @property
    def register_count(self) -> int:
        return len(self.registrants)


class Club(BaseModel):
    name: str = Field(min_length=2, max_length=100, description="Name of the club")
    members: list[Member | Freelancer | Researcher] = Field(
        default_factory=list, description="List of club members"
    )
    partner_companies: list[PartnerCompany] = Field(
        default_factory=list, description="List of partner companies"
    )
    events: list[Event] = Field(
        default_factory=list, description="List of events organized by the club"
    )
