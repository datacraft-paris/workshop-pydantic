from pydantic import BaseModel

from .company import PartnerCompany, Company


class Person(...):
    name: str
    email: str


class Member(Person):
    id: ...
    company: PartnerCompany


class Freelancer(...):
    id: int
    specialty: str
    companies: list[... | ...]
    daily_rate: ...


... Researcher(...):
    id: int
    field_of_study: ...
    ...
