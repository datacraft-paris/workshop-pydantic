from pydantic import BaseModel, computed_field, Field
from datetime import datetime

from .people import Member, Freelancer, Researcher
from .enums import EventType
