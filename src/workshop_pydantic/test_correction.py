from correction import (
    Member,
    PartnerCompany,
    Employee,
    Event,
    Club,
    Intern,
    EducationLevel,
    Department,
    Project,
    Priority,
    TaskType,
    Task,
)
from datetime import datetime, timedelta
from pydantic import ValidationError


"""
This file is a set of tests to verify the proper functioning of the classes defined
in the 'correction' module. It only tests and validates the expected functionality.
To run the tests, simply run this file.
"""


# ======================================================================
# Step 1: Test for Member class
# ======================================================================
def test_member():
    """Test the creation of a Member instance."""
    member = Member(id=1, name="Paul", email="paul@example.com")
    print(member)
    return True


# ======================================================================
# Step 2: Test for PartnerCompany class
# ======================================================================
def test_partner_company():
    """Test the creation of a PartnerCompany instance."""
    company = PartnerCompany(
        name="OpenAI",
        website="https://openai.com",
        sector="Artificial Intelligence",
        employee_count=1000,
        is_active=True,
    )
    print(company)
    return True


# ======================================================================
# Step 3: Test for Employee class
# ======================================================================
def test_valid_employee():
    """Test the creation of a valid Employee instance."""
    emp = Employee(name="Alice", age=30, salary=40000)
    print(emp)
    return True


def test_invalid_name():
    """Test the validation of an Employee name containing digits."""
    try:
        Employee(name="Al1ce", age=30, salary=40000)
        print("test_invalid_name failed: no error raised")
        return False
    except ValidationError as e:
        print(f"test_invalid_name caught error as expected: {e}")
        return True


def test_invalid_salary():
    """Test the validation of an Employee salary that is too low."""
    try:
        Employee(name="Bob", age=30, salary=1000)
        print("test_invalid_salary failed: no error raised")
        return False
    except ValidationError as e:
        print(f"test_invalid_salary caught error as expected: {e}")
        return True


# ======================================================================
# Step 4: Test for Event class
# ======================================================================
def test_event_date_validation():
    """Test the creation of an Event instance with valid dates."""
    start = datetime.now()
    end = start + timedelta(hours=2)

    event = Event(
        name="DataCraft Awards",
        start_time=start,
        end_time=end,
        location="Paris",
        registered_count=1500,
    )
    print(event)
    return True


def test_event_invalid_date_validation():
    """Test the validation of an Event with an invalid end date."""
    start = datetime.now()
    try:
        Event(
            name="Invalid Event",
            start_time=start,
            end_time=start - timedelta(hours=1),
            location="Paris",
            registered_count=10,
        )
        print("test_event_invalid_date_validation failed: no error raised")
        return False
    except ValidationError as e:
        print(f"test_event_invalid_date_validation caught error as expected: {e}")
        return True


# ======================================================================
# Step 5: Test for Club class
# ======================================================================
def test_club():
    """Test the creation of a Club instance with members, partners, and events."""
    members = [
        Member(id=1, name="Paul", email="paul@example.com"),
        Member(id=2, name="Raphaël", email="raphaël@example.com"),
    ]

    partners = [
        PartnerCompany(
            name="OpenAI",
            website="https://openai.com",
            sector="AI",
            employee_count=1000,
        ),
        PartnerCompany(
            name="DataCorp",
            website=None,
            sector="Data Science",
            employee_count=50,
            is_active=False,
        ),
    ]

    events = [
        Event(
            name="Hackathon",
            start_time=datetime.now(),
            end_time=datetime.now() + timedelta(hours=8),
            location="Remote",
            registered_count=20,
        ),
        Event(
            name="Workshop",
            start_time=datetime.now() + timedelta(days=7),
            end_time=datetime.now() + timedelta(days=7, hours=3),
            location="Paris",
            registered_count=15,
        ),
    ]

    club = Club(
        name="DataCraft", members=members, partner_companies=partners, events=events
    )

    print("Club instance:\n", club)
    print("\nPartner companies:", club.partner_companies)
    return True


# ======================================================================
# Step 6: Test for Intern class
# ======================================================================
def test_valid_intern():
    """Test the creation of a valid Intern instance."""
    intern = Intern(
        name="Chloe",
        age=22,
        education_level=EducationLevel.MASTER,
        department=Department.AI,
    )
    print(intern)
    return True


def test_invalid_education_level():
    """Test the validation of an Intern with an invalid education level."""
    try:
        Intern(
            name="Lucas",
            age=21,
            education_level="kindergarten",
            department=Department.DATA,
        )
        print("test_invalid_education_level failed: no error raised")
        return False
    except ValidationError as e:
        print("test_invalid_education_level caught error as expected:", e)
        return True


# ======================================================================
# Step 7: Test for Project class
# ======================================================================
def test_project_with_employee():
    """Test the creation of a Project instance assigned to an Employee."""
    emp = Employee(name="Alice", age=28, salary=45000)
    project = Project(
        name="AI Optimizer",
        client="OpenAI",
        assigned_to=emp,
        deadline=datetime.now(),
        budget_euros=100000.0,
        documentation_link="https://docs.openai.com/project",
    )
    print(project)
    return True


# ======================================================================
# Step 8: Test for Task class
# ======================================================================
def test_valid_task():
    """Test the creation of a valid Task instance."""
    emp = Employee(name="Alice", age=30, salary=40000)
    project = Project(
        name="AI Optimizer",
        client="OpenAI",
        assigned_to=emp,
        deadline=datetime.now() + timedelta(days=30),
        budget_euros=100000.0,
        documentation_link="https://docs.openai.com/project",
    )
    task = Task(
        title="Implement new feature",
        task_type=TaskType.FEATURE,
        assigned_to=emp,
        priority=Priority.HIGH,
        due_date=datetime.now() + timedelta(days=10),
        project=project,
    )
    print("Valid task created successfully:", task)
    return True


def test_invalid_title():
    """Test the validation of a Task with an invalid title."""
    try:
        emp = Employee(name="Alice", age=30, salary=40000)
        project = Project(
            name="AI Optimizer",
            client="OpenAI",
            assigned_to=emp,
            deadline=datetime.now() + timedelta(days=30),
            budget_euros=100000.0,
            documentation_link="https://docs.openai.com/project",
        )
        Task(title="Fix", task_type=TaskType.BUGFIX, assigned_to=emp, project=project)
        print("test_invalid_title failed: no error raised")
        return False
    except ValidationError as e:
        print(f"test_invalid_title caught error as expected: {e}")
        return True


def test_invalid_due_date():
    """Test the validation of a Task with an invalid due date."""
    try:
        emp = Employee(name="Alice", age=30, salary=40000)
        project = Project(
            name="AI Optimizer",
            client="OpenAI",
            assigned_to=emp,
            deadline=datetime.now() + timedelta(days=30),
            budget_euros=100000.0,
            documentation_link="https://docs.openai.com/project",
        )
        Task(
            title="Implement new feature",
            task_type=TaskType.FEATURE,
            assigned_to=emp,
            due_date=datetime.now() - timedelta(days=1),
            project=project,
        )
        print("test_invalid_due_date failed: no error raised")
        return False
    except ValidationError as e:
        print(f"test_invalid_due_date caught error as expected: {e}")
        return True


def test_invalid_priority_for_documentation():
    """Test the validation of a Task with invalid priority for documentation."""
    try:
        emp = Employee(name="Alice", age=30, salary=40000)
        project = Project(
            name="AI Optimizer",
            client="OpenAI",
            assigned_to=emp,
            deadline=datetime.now() + timedelta(days=30),
            budget_euros=100000.0,
            documentation_link="https://docs.openai.com/project",
        )
        Task(
            title="Write documentation",
            task_type=TaskType.DOCUMENTATION,
            assigned_to=emp,
            priority=Priority.HIGH,
            project=project,
        )
        print("test_invalid_priority_for_documentation failed: no error raised")
        return False
    except ValidationError as e:
        print(f"test_invalid_priority_for_documentation caught error as expected: {e}")
        return True


# ======================================================================
# Execute all tests
# ======================================================================
tests = [
    test_member,
    test_partner_company,
    test_valid_employee,
    test_invalid_name,
    test_invalid_salary,
    test_event_date_validation,
    test_event_invalid_date_validation,
    test_club,
    test_valid_intern,
    test_invalid_education_level,
    test_project_with_employee,
    test_valid_task,
    test_invalid_title,
    test_invalid_due_date,
    test_invalid_priority_for_documentation,
]

all_tests_passed = True
count = 0
for test in tests:
    print(f"\n>>> {test.__name__} 🚀")
    try:
        if test():
            count += 1
            print(f"+++ {test.__name__} passed ✅ ({count}/{len(tests)})")
        else:
            print(f"!!! {test.__name__} failed ❌ ({count}/{len(tests)})")
            all_tests_passed = False
            break
    except Exception as e:
        print(f"!!! {test.__name__} failed ❌: {e} ({count}/{len(tests)})")
        all_tests_passed = False
        break

if all_tests_passed:
    print("\nAll tests passed successfully! 🎉")
