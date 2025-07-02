import sys
from pathlib import Path
from pydantic import BaseModel, HttpUrl
from datetime import datetime

# Add the src/ folder to sys.path
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from workshop_pydantic.model_1.people import Person, Member, Freelancer, Researcher
from workshop_pydantic.model_1.company import Company, PartnerCompany
from workshop_pydantic.model_1.event import Event
from workshop_pydantic.model_1.club import Club

# Test data
test_person_data = {
    "name": "John Doe",
    "email": "john.doe@example.com"
}

test_company_data = {
    "name": "Tech Corp",
    "website": HttpUrl("http://techcorp.example.com"),
    "sector": "Technology",
    "employee_count": 100
}

test_partner_company_data = {
    **test_company_data,
    "is_active": True
}

test_member_data = {
    **test_person_data,
    "id": 1,
    "company": PartnerCompany(**test_partner_company_data)
}

test_freelancer_data = {
    **test_person_data,
    "id": 2,
    "specialty": "Software Development",
    "companies": [Company(**test_company_data)],
    "daily_rate": 200
}

test_researcher_data = {
    **test_person_data,
    "id": 3,
    "field_of_study": "Computer Science",
    "number_of_articles": 5
}

test_event_data = {
    "name": "Tech Conference",
    "event_type": "Conference",
    "registrants": [],
    "location": "Virtual",
    "start_time": datetime.now(),
    "end_time": datetime.now()
}

test_club_data = {
    "members": [],
    "partner_companies": [],
    "events": []
}

def test_person_initialization():
    person = Person(**test_person_data)
    assert person.name == test_person_data["name"]
    assert person.email == test_person_data["email"]

def test_company_initialization():
    company = Company(**test_company_data)
    assert company.name == test_company_data["name"]
    assert company.website == test_company_data["website"]
    assert company.sector == test_company_data["sector"]
    assert company.employee_count == test_company_data["employee_count"]

def test_partner_company_initialization():
    partner_company = PartnerCompany(**test_partner_company_data)
    assert partner_company.is_active == test_partner_company_data["is_active"]

def test_member_initialization():
    member = Member(**test_member_data)
    assert member.id == test_member_data["id"]
    assert member.company.is_active == test_member_data["company"].is_active

def test_freelancer_initialization():
    freelancer = Freelancer(**test_freelancer_data)
    assert freelancer.id == test_freelancer_data["id"]
    assert freelancer.specialty == test_freelancer_data["specialty"]
    assert len(freelancer.companies) == len(test_freelancer_data["companies"])
    assert freelancer.daily_rate == test_freelancer_data["daily_rate"]

def test_researcher_initialization():
    researcher = Researcher(**test_researcher_data)
    assert researcher.id == test_researcher_data["id"]
    assert researcher.field_of_study == test_researcher_data["field_of_study"]
    assert researcher.number_of_articles == test_researcher_data["number_of_articles"]

def test_event_initialization():
    event = Event(**test_event_data)
    assert event.name == test_event_data["name"]
    assert event.location == test_event_data["location"]
    assert event.register_count == len(test_event_data["registrants"])

def test_club_initialization():
    club = Club(**test_club_data)
    assert len(club.members) == len(test_club_data["members"])
    assert len(club.partner_companies) == len(test_club_data["partner_companies"])
    assert len(club.events) == len(test_club_data["events"])
