import sys
from pathlib import Path
import pytest
from datetime import datetime
from pydantic import HttpUrl, ValidationError

# Add the root directory to the Python path
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from workshop_pydantic.model_3.people import Person, Freelancer, Researcher
from workshop_pydantic.model_3.company import Company, PartnerCompany
from workshop_pydantic.model_3.event import Event
from workshop_pydantic.model_3.club import Club
from workshop_pydantic.model_3.enums import Sector, Specialty, FieldOfStudy, EventType


def test_person_field_constraints():
    # Test valid person
    person = Person(name="John Doe", email="john.doe@example.com")
    assert person.name == "John Doe"
    assert person.email == "john.doe@example.com"

    # Test name constraints
    with pytest.raises(ValidationError):
        Person(name="J", email="john.doe@example.com")  # Name too short
    with pytest.raises(ValidationError):
        Person(name="J" * 51, email="john.doe@example.com")  # Name too long

    # Test email constraints
    with pytest.raises(ValidationError):
        Person(name="John Doe", email="invalid-email")  # Invalid email format


def test_company_field_constraints():
    # Test valid company
    company = Company(
        name="Tech Corp",
        website=HttpUrl("http://techcorp.example.com"),
        sector=Sector.TECHNOLOGY,
        employee_count=100,
    )
    assert company.name == "Tech Corp"
    assert company.website == HttpUrl("http://techcorp.example.com")
    assert company.sector == Sector.TECHNOLOGY
    assert company.employee_count == 100

    # Test name constraints
    with pytest.raises(ValidationError):
        Company(
            name="T",
            website=HttpUrl("http://techcorp.example.com"),
            sector=Sector.TECHNOLOGY,
            employee_count=100,
        )  # Name too short
    with pytest.raises(ValidationError):
        Company(
            name="T" * 101,
            website=HttpUrl("http://techcorp.example.com"),
            sector=Sector.TECHNOLOGY,
            employee_count=100,
        )  # Name too long

    # Test employee_count constraints
    with pytest.raises(ValidationError):
        Company(
            name="Tech Corp",
            website=HttpUrl("http://techcorp.example.com"),
            sector=Sector.TECHNOLOGY,
            employee_count=0,
        )  # Too few employees
    with pytest.raises(ValidationError):
        Company(
            name="Tech Corp",
            website=HttpUrl("http://techcorp.example.com"),
            sector=Sector.TECHNOLOGY,
            employee_count=100000,
        )  # Too many employees


def test_partner_company_defaults():
    company = PartnerCompany(
        name="Partner Corp", sector=Sector.TECHNOLOGY, employee_count=50
    )
    assert company.is_active is True  # Default value


def test_freelancer_field_constraints():
    company = Company(
        name="Tech Corp",
        website=HttpUrl("http://techcorp.example.com"),
        sector=Sector.TECHNOLOGY,
        employee_count=100,
    )
    freelancer = Freelancer(
        name="John Smith",
        email="john.smith@example.com",
        id=1,
        specialty=Specialty.SOFTWARE_DEVELOPMENT,
        companies=[company],
        daily_rate=300,
    )
    assert freelancer.daily_rate == 300
    assert isinstance(freelancer.companies, list)  # Default factory

    # Test daily_rate constraints
    with pytest.raises(ValidationError):
        Freelancer(
            name="John Smith",
            email="john.smith@example.com",
            id=1,
            specialty=Specialty.SOFTWARE_DEVELOPMENT,
            companies=[company],
            daily_rate=299,
        )  # Not a multiple of 50
    with pytest.raises(ValidationError):
        Freelancer(
            name="John Smith",
            email="john.smith@example.com",
            id=1,
            specialty=Specialty.SOFTWARE_DEVELOPMENT,
            companies=[company],
            daily_rate=-100,
        )  # Negative rate


def test_researcher_defaults_and_constraints():
    researcher = Researcher(
        name="Alice Brown",
        email="alice.brown@example.com",
        id=1,
        field_of_study=FieldOfStudy.COMPUTER_SCIENCE,
    )
    assert researcher.number_of_articles == 0  # Default value

    with pytest.raises(ValidationError):
        Researcher(
            name="Alice Brown",
            email="alice.brown@example.com",
            id=-1,
            field_of_study=FieldOfStudy.COMPUTER_SCIENCE,
            number_of_articles=-1,
        )  # Negative id
    with pytest.raises(ValidationError):
        Researcher(
            name="Alice Brown",
            email="alice.brown@example.com",
            id=1,
            field_of_study=FieldOfStudy.COMPUTER_SCIENCE,
            number_of_articles=-1,
        )  # Negative articles
    with pytest.raises(ValidationError):
        Researcher(
            name="Alice Brown",
            email="alice.brown@example.com",
            id=1,
            field_of_study=FieldOfStudy.COMPUTER_SCIENCE,
            number_of_articles=float("inf"),
        )  # NaN articles


def test_event_field_constraints():
    event = Event(
        event_type=EventType.WORKSHOP,
        registrants=[],
        location="Virtual",
        start_time=datetime.now(),
        end_time=datetime.now(),
    )
    assert isinstance(event.registrants, list)  # Default factory
    assert event.location == "Virtual"

    with pytest.raises(ValidationError):
        Event(
            event_type=EventType.WORKSHOP,
            registrants=[],
            location="V",
            start_time=datetime.now(),
            end_time=datetime.now(),
        )  # Location too short
    with pytest.raises(ValidationError):
        Event(
            event_type=EventType.WORKSHOP,
            registrants=[],
            location="V" * 201,
            start_time=datetime.now(),
            end_time=datetime.now(),
        )  # Location too long


def test_club_field_constraints():
    club = Club(members=[], partner_companies=[], events=[])
    assert isinstance(club.members, list)  # Default factory
    assert isinstance(club.partner_companies, list)  # Default factory
    assert isinstance(club.events, list)  # Default factory
