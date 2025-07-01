from pydantic import BaseModel, HttpUrl, computed_field
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
    name: str
    email: str


class Company(BaseModel):
    name: str
    website: HttpUrl | None
    sector: Sector
    employee_count: int


class PartnerCompany(Company):
    is_active: bool


class Member(Person):
    id: int
    company: PartnerCompany


class Freelancer(Person):
    id: int
    specialty: Specialty
    company: list[PartnerCompany | Company]
    daily_rate: int | None


class Researcher(Person):
    id: int
    field_of_study: FieldOfStudy
    company: list[PartnerCompany | Company]
    number_of_articles: int


class Event(BaseModel):
    name: str
    event_type: EventType
    registrants: list[Member | Freelancer | Researcher]
    location: str
    start_time: datetime
    end_time: datetime

    @computed_field
    @property
    def register_count(self) -> int:
        return len(self.registrants)


class Club(BaseModel):
    name: str
    members: list[Member | Freelancer | Researcher]
    partner_companies: list[PartnerCompany]
    events: list[Event]
