from enum import Enum


class Sector(str, Enum):
    TECHNOLOGY = "Technology"
    HEALTHCARE = "Healthcare"
    EDUCATION = "Education"
    FINANCE = "Finance"


class Specialty(str, Enum):
    SOFTWARE_DEVELOPMENT = "Software Development"
    DATA_SCIENCE = "Data Science"
    CYBERSECURITY = ...
    DEVOPS = "DevOps"


class FieldOfStudy(str, ...):
    COMPUTER_SCIENCE = "Computer Science"
    ... = "Biology"
    PHYSICS = "Physics"
    ... = "Chemistry"


class EventType(..., Enum):
    WORKSHOP = "Workshop"
    CONFERENCE = "Conference"
    ...
    ...
