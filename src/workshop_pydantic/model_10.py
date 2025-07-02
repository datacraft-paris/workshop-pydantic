from pydantic import BaseModel, HttpUrl, computed_field
from datetime import datetime


class Person(BaseModel):
    name: str
    email: str


class Company(BaseModel):
    name: str
    website: HttpUrl | None
    sector: str
    employee_count: int


class PartnerCompany(Company):
    is_active: bool


class Member(Person):
    id: int
    company: PartnerCompany


class Freelancer(Person):
    id: int
    specialty: str
    companies: list[PartnerCompany | Company]
    daily_rate: int | None


class Researcher(Person):
    id: int
    field_of_study: str
    number_of_articles: int


class Event(BaseModel):
    name: str
    registrants: list[Member | Freelancer | Researcher]
    location: str
    start_time: datetime
    end_time: datetime

    @computed_field
    @property
    def register_count(self) -> int:
        return len(self.registrants)


class Club(BaseModel):
    members: list[Member | Freelancer | Researcher]
    partner_companies: list[PartnerCompany]
    events: list[Event]
