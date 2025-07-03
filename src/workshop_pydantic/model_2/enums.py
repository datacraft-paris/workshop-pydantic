from enum import Enum


class Sector(str, Enum):
    TECHNOLOGY = "Technology"
    HEALTHCARE = "Healthcare"
    EDUCATION = ...
    FINANCE = ...


class Specialty(str, Enum):
    SOFTWARE_DEVELOPMENT = "Software Development"
    DATA_SCIENCE = ...



class FieldOfStudy(str, Enum):
    COMPUTER_SCIENCE = "Computer Science"
    ...


class EventType(str, Enum):
    ...
