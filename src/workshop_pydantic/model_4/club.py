from pydantic import BaseModel, Field, field_validator, model_validator, ValidationInfo

from .people import Member, Freelancer, Researcher
from .company import PartnerCompany
from .event import Event
