from pydantic import (
    BaseModel,
    Field,
    HttpUrl,
    computed_field,
    field_validator,
    model_validator,
    ValidationInfo,
)
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
    NETWORKING = "Networking"
    DATATHON = "Datathon"


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


class Company(BaseModel):
    name: str = Field(min_length=2, max_length=100, description="Name of the company")
    website: HttpUrl | None = Field(
        default=None, description="Official website URL of the company"
    )
    sector: Sector = Field(description="Business sector of the company")
    employee_count: int = Field(
        gt=0, lt=100000, description="Number of employees in the company"
    )

    @field_validator("website")
    @classmethod
    def website_required_for_finance(cls, value, info: ValidationInfo):
        sector = info.data.get("sector")
        if sector == Sector.FINANCE and value is None:
            raise ValueError("Finance companies must have a website")
        return value


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
    companies: list[PartnerCompany | Company] = Field(
        default_factory=list, description="Companies associated with the freelancer"
    )
    daily_rate: int | None = Field(
        gt=0,
        multiple_of=50,
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

    @model_validator(mode="before")
    @classmethod
    def check_event_data(cls, data):
        if "start_time" in data and "end_time" in data:
            if data["start_time"] >= data["end_time"]:
                raise ValueError("Start time must be before end time")
        return data

    @model_validator(mode="after")
    def check_event_registration_and_speakers(self):
        if self.event_type == EventType.DATATHON and len(self.registrants) < 10:
            raise ValueError(
                "Datathon events must have at least 10 registered attendees"
            )
        if not self.registrants and self.event_type != EventType.NETWORKING:
            raise ValueError("Non-networking events must have at least one registrant")
        return self


class Club(BaseModel):
    members: list[Member | Freelancer | Researcher] = Field(
        default_factory=list, description="List of club members"
    )
    partner_companies: list[PartnerCompany] = Field(
        default_factory=list, description="List of partner companies"
    )
    events: list[Event] = Field(
        default_factory=list, description="List of events organized by the club"
    )

    @field_validator("events")
    @classmethod
    def validate_events(cls, value, info: ValidationInfo):
        members = info.data.get("members", [])
        if len(members) > 100 and len(value) < 3:
            raise ValueError(
                "Clubs with more than 100 members must have at least 3 events"
            )
        return value

    @model_validator(mode="before")
    @classmethod
    def check_club_data(cls, data):
        if (
            not data.get("members")
            and not data.get("partner_companies")
            and not data.get("events")
        ):
            raise ValueError(
                "A club must have at least one member, partner company, or event"
            )
        return data
