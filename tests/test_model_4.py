import sys
from pathlib import Path
import pytest
from datetime import datetime, timedelta
from pydantic import HttpUrl, ValidationError

# Add the root directory to the Python path
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from workshop_pydantic.model_4.people import Person, Member, Freelancer
from workshop_pydantic.model_4.company import Company, PartnerCompany
from workshop_pydantic.model_4.event import Event
from workshop_pydantic.model_4.club import Club
from workshop_pydantic.model_4.enums import Sector, Specialty, EventType


def test_person_name_validator():
    # Test valid name
    person = Person(name="John Doe", email="john.doe@example.com")
    assert person.name == "John Doe"

    # Test invalid name with special characters
    with pytest.raises(ValidationError):
        Person(name="John Doe123", email="john.doe@example.com")


def test_company_website_validator():
    # Test valid company with website
    company = Company(
        name="Finance Corp",
        website=HttpUrl("http://financecorp.example.com"),
        sector=Sector.FINANCE,
        employee_count=100,
    )
    assert company.website == HttpUrl("http://financecorp.example.com")

    # Test finance company without website
    with pytest.raises(ValidationError) as excinfo:
        Company(
            name="Finance Corp", website=None, sector=Sector.FINANCE, employee_count=100
        )


def test_freelancer_daily_rate_validator():
    company = Company(
        name="Tech Corp",
        website=HttpUrl("http://techcorp.example.com"),
        sector=Sector.TECHNOLOGY,
        employee_count=100,
    )

    # Test valid daily rate for Software Development
    freelancer = Freelancer(
        name="John Smith",
        email="john.smith@example.com",
        id=1,
        specialty=Specialty.SOFTWARE_DEVELOPMENT,
        companies=[company],
        daily_rate=300,
    )
    assert freelancer.daily_rate == 300

    # Cas invalides - doivent lever ValidationError
    with pytest.raises(ValidationError):
        Freelancer(specialty=Specialty.SOFTWARE_DEVELOPMENT, daily_rate=299)
    with pytest.raises(ValidationError):
        Freelancer(specialty=Specialty.DATA_SCIENCE, daily_rate=300)  # < 350
    with pytest.raises(ValidationError):
        Freelancer(specialty=Specialty.CYBERSECURITY, daily_rate=350)  # < 400
    with pytest.raises(ValidationError):
        Freelancer(specialty=Specialty.DEVOPS, daily_rate=300)  # < 375


def test_event_validators():
    member = Member(
        name="Jane Doe",
        email="jane.doe@example.com",
        id=1,
        company=PartnerCompany(
            name="Partner Corp", sector=Sector.TECHNOLOGY, employee_count=50
        ),
    )

    # Test valid event
    start_time = datetime.now()
    end_time = start_time + timedelta(hours=2)
    event = Event(
        name="Tech Conference",
        event_type=EventType.WORKSHOP,
        registrants=[member],
        location="Virtual",
        start_time=start_time,
        end_time=end_time,
    )
    assert event.register_count == 1

    # Test invalid event with start_time after end_time
    with pytest.raises(ValidationError):
        Event(
            name="Tech Conference",
            event_type=EventType.WORKSHOP,
            registrants=[member],
            location="Virtual",
            start_time=end_time,
            end_time=start_time,
        )

    # Test Datathon event with insufficient registrants
    with pytest.raises(ValidationError):
        Event(
            name="Data Event",
            event_type=EventType.DATATHON,
            registrants=[],
            location="Virtual",
            start_time=start_time,
            end_time=end_time,
        )

    # Test Datathon event with insufficient registrants for a none conference event
    with pytest.raises(ValidationError):
        Event(
            name="Data Event",
            event_type=EventType.WORKSHOP,
            registrants=[],
            location="Virtual",
            start_time=start_time,
            end_time=end_time,
        )


def test_club_validators():
    # Create a sample member and event for testing
    member = Member(
        name="JaneDoe",
        email="jane.doe@example.com",
        id=1,
        company=PartnerCompany(
            name="PartnerCorp", sector=Sector.TECHNOLOGY, employee_count=50
        ),
    )
    event = Event(
        name="TechConference",
        event_type=EventType.WORKSHOP,
        registrants=[member],
        location="Virtual",
        start_time=datetime.now(),
        end_time=datetime.now() + timedelta(hours=2),
    )

    # Test valid club
    club = Club(members=[member], partner_companies=[], events=[event, event, event])
    assert len(club.events) == 3

    # Test club with more than 100 members and insufficient events
    members = [
        Member(
            name=f"Member{chr(65 + (i // 26))}{chr(65 + (i % 26))}",
            email=f"member{i}@example.com",
            id=i + 1,
            company=PartnerCompany(
                name="PartnerCorp", sector=Sector.TECHNOLOGY, employee_count=50
            ),
        )
        for i in range(101)
    ]
    with pytest.raises(ValidationError):
        Club(members=members, partner_companies=[], events=[event])

    # Test club with no members, partner companies, or events
    with pytest.raises(ValidationError):
        Club(members=[], partner_companies=[], events=[])
