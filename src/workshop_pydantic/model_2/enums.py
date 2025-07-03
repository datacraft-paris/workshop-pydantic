from enum import Enum


class Sector(str, Enum):
    TECHNOLOGY = "Technology"
    HEALTHCARE = "Healthcare"
    EDUCATION = ...
    FINANCE = ...


class Specialty(str, ...):
    SOFTWARE_DEVELOPMENT = "Software Development"
    DATA_SCIENCE = ...



class FieldOfStudy(..., Enum):
    COMPUTER_SCIENCE = "Computer Science"
    ...


class EventType(...):
    ...
