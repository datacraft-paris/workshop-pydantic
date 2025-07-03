from pydantic import BaseModel, Field, field_validator, ValidationInfo

from .company import PartnerCompany, Company
from .enums import Specialty, FieldOfStudy
