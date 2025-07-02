from pydantic import BaseModel

from .company import PartnerCompany, Company


class Person(BaseModel):
    name: ...
    ...


class Member(...):
    ...


class Freelancer(...):
    id: int
    specialty: str
    companies: ...
    daily_rate: ...


class ...
