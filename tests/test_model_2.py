import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from workshop_pydantic.model_2.people import Freelancer, Researcher
from workshop_pydantic.model_2.company import Company
from workshop_pydantic.model_2.event import Event
from workshop_pydantic.model_2.enums import Sector, Specialty, FieldOfStudy, EventType
from datetime import datetime
from pydantic import HttpUrl


def test_enum_values_case_insensitive():
    # Test Sector enum
    assert Sector.TECHNOLOGY.value.lower() == "technology"
    assert Sector.HEALTHCARE.value.lower() == "healthcare"
    assert Sector.EDUCATION.value.lower() == "education"
    assert Sector.FINANCE.value.lower() == "finance"

    # Test Specialty enum
    assert Specialty.SOFTWARE_DEVELOPMENT.value.lower() == "software development"
    assert Specialty.DATA_SCIENCE.value.lower() == "data science"
    assert Specialty.CYBERSECURITY.value.lower() == "cybersecurity"
    assert Specialty.DEVOPS.value.lower() == "devops"

    # Test FieldOfStudy enum
    assert FieldOfStudy.COMPUTER_SCIENCE.value.lower() == "computer science"
    assert FieldOfStudy.BIOLOGY.value.lower() == "biology"
    assert FieldOfStudy.PHYSICS.value.lower() == "physics"
    assert FieldOfStudy.CHEMISTRY.value.lower() == "chemistry"

    # Test EventType enum
    assert EventType.WORKSHOP.value.lower() == "workshop"
    assert EventType.CONFERENCE.value.lower() == "conference"
    assert EventType.SEMINAR.value.lower() == "seminar"
    assert EventType.DATATHON.value.lower() == "datathon"


def test_company_sector_enum():
    company = Company(
        name="Tech Corp",
        website=HttpUrl("http://techcorp.example.com"),
        sector=Sector.TECHNOLOGY,
        employee_count=100,
    )
    assert company.sector == Sector.TECHNOLOGY


def test_freelancer_specialty_enum():
    company = Company(
        name="Tech Corp",
        website=HttpUrl("http://techcorp.example.com"),
        sector=Sector.TECHNOLOGY,
        employee_count=100,
    )
    freelancer = Freelancer(
        name="John Smith",
        email="john.smith@example.com",
        id=2,
        specialty=Specialty.SOFTWARE_DEVELOPMENT,
        companies=[company],
        daily_rate=300,
    )
    assert freelancer.specialty == Specialty.SOFTWARE_DEVELOPMENT


def test_researcher_field_of_study_enum():
    researcher = Researcher(
        name="Alice Brown",
        email="alice.brown@example.com",
        id=3,
        field_of_study=FieldOfStudy.COMPUTER_SCIENCE,
        number_of_articles=5,
    )
    assert researcher.field_of_study == FieldOfStudy.COMPUTER_SCIENCE


def test_event_type_enum():
    event = Event(
        name="Tech Conference",
        event_type=EventType.WORKSHOP,
        registrants=[],
        location="Virtual",
        start_time=datetime.now(),
        end_time=datetime.now(),
    )
    assert event.event_type == EventType.WORKSHOP
