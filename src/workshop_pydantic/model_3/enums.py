from enum import Enum


class Sector(str, Enum):
    TECHNOLOGY = "Technology"
    HEALTHCARE = "Healthcare"
    EDUCATION = "Education"
    FINANCE = "Finance"


class Specialty(str, Enum):
    SOFTWARE_DEVELOPMENT = "Software Development"
    DATA_SCIENCE = "Data Science"
    CYBERSECURITY = "Cybersecurity"
    DEVOPS = "DevOps"


class FieldOfStudy(str, Enum):
    COMPUTER_SCIENCE = "Computer Science"
    BIOLOGY = "Biology"
    PHYSICS = "Physics"
    CHEMISTRY = "Chemistry"


class EventType(str, Enum):
    WORKSHOP = "Workshop"
    CONFERENCE = "Conference"
    SEMINAR = "Seminar"
    DATATHON = "Datathon"
