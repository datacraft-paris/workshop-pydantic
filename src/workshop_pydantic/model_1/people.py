from pydantic import BaseModel

from .company import PartnerCompany, Company


class Person(BaseModel):
    name: str
    email: str


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
