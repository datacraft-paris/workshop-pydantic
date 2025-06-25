try:
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
except ImportError:
    pass

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


def test_member_with_valid_email():
    """Test the creation of a Member instance with a valid email."""
    try:
        member = Member(id=1, name="Paul", email="paul@example.com")
        print("Valid Member created successfully:", member)
        return True
    except Exception as e:
        print(f"test_member_with_valid_email failed: {e}")
        return False


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


def test_partner_company_with_invalid_employee_count():
    """Test the validation of a PartnerCompany with an invalid employee count."""
    try:
        PartnerCompany(
            name="OpenAI",
            website="https://openai.com",
            sector="Artificial Intelligence",
            employee_count=0,
            is_active=True,
        )
        print(
            "test_partner_company_with_invalid_employee_count failed: no error raised"
        )
        return False
    except ValidationError as e:
        print(
            f"test_partner_company_with_invalid_employee_count caught error as expected: {e}"
        )
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


def test_employee_with_minimum_age():
    """Test the creation of an Employee instance with the minimum valid age."""
    Employee(name="Bob", age=19, salary=20000)
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


def test_event_with_zero_registered_count():
    """Test the creation of an Event instance with zero registered attendees."""
    start = datetime.now()
    end = start + timedelta(hours=2)

    event = Event(
        name="DataCraft Awards",
        start_time=start,
        end_time=end,
        location="Paris",
        registered_count=0,
    )
    print(event)
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


def test_club_with_empty_lists():
    """Test the creation of a Club instance with empty lists of members and partner companies."""
    Club(name="EmptyClub", members=[], partner_companies=[], events=None)
    return True


def test_club_with_event_list():
    """Test the creation of a Club instance with a list of events."""
    try:
        members = [
            Member(id=1, name="Paul", email="paul@example.com"),
        ]

        partners = [
            PartnerCompany(
                name="DataCorp",
                website=None,
                sector="Data Science",
                employee_count=50,
                is_active=False,
            )
        ]

        events = [
            Event(
                name="Hackathon",
                start_time=datetime.now(),
                end_time=datetime.now() + timedelta(hours=8),
                location="Remote",
                registered_count=20,
            )
        ]

        club = Club(
            name="EventfulClub",
            members=members,
            partner_companies=partners,
            events=events,  # Setting events to a list of Event objects
        )

        print("Club with event list created successfully:", club)
        return True
    except Exception as e:
        print(f"test_club_with_event_list failed: {e}")
        return False


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


def test_intern_with_default_department():
    """Test the creation of an Intern instance with the default department."""
    intern = Intern(
        name="Chloe",
        age=22,
        education_level=EducationLevel.MASTER,
    )
    print(intern)
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


def test_project_with_intern():
    """Test the creation of a Project instance assigned to an Intern."""
    intern = Intern(
        name="Chloe",
        age=22,
        education_level=EducationLevel.MASTER,
        department=Department.DATA,
    )
    project = Project(
        name="Data Analysis",
        client="DataCorp",
        assigned_to=intern,
        deadline=datetime.now(),
        budget_euros=50000.0,
        documentation_link="https://docs.datacorp.com/project",
    )
    print(project)
    return True


def test_project_with_positive_budget():
    """Test the creation of a Project instance with a positive budget."""
    try:
        emp = Employee(name="Alice", age=28, salary=45000)
        project = Project(
            name="AI Optimizer",
            client="OpenAI",
            assigned_to=emp,
            budget_euros=100000.0,  # Positive budget
            documentation_link="https://docs.openai.com/project",
        )
        print("Project with positive budget created successfully:", project)
        return True
    except Exception as e:
        print(f"test_project_with_positive_budget failed: {e}")
        return False


def test_project_with_negative_budget():
    """Test the validation of a Project with a negative budget."""
    try:
        emp = Employee(name="Alice", age=28, salary=45000)
        Project(
            name="AI Optimizer",
            client="OpenAI",
            assigned_to=emp,
            budget_euros=-100000.0,  # Negative budget
            documentation_link="https://docs.openai.com/project",
        )
        print("test_project_with_negative_budget failed: no error raised")
        return False
    except ValidationError as e:
        print(f"test_project_with_negative_budget caught error as expected: {e}")
        return True


def test_project_with_string_documentation_link():
    """Test the creation of a Project instance with a string as documentation link."""
    try:
        emp = Employee(name="Alice", age=28, salary=45000)
        documentation_link = "Internal reference to project docs"
        project = Project(
            name="AI Optimizer",
            client="OpenAI",
            assigned_to=emp,
            documentation_link=documentation_link,  # String as documentation link
        )

        # Vérifie que l'attribut documentation_link existe et a la bonne valeur
        assert hasattr(
            project, "documentation_link"
        ), "Project instance has no attribute 'documentation_link'"
        assert (
            project.documentation_link == documentation_link
        ), f"Expected documentation_link to be '{documentation_link}', but got '{project.documentation_link}'"

        print("Project with string documentation link created successfully:", project)
        return True
    except Exception as e:
        print(f"test_project_with_string_documentation_link failed: {e}")
        return False


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


def test_task_title_validation():
    """Test that a generic task title raises a validation error."""
    try:
        emp = Employee(name="Alice", age=30, salary=45000)
        project = Project(
            name="AI Optimizer",
            client="OpenAI",
            assigned_to=emp,
            deadline=datetime.now() + timedelta(days=30),
            budget_euros=100000.0,
            documentation_link="https://docs.openai.com/project",
        )

        # Tentative de création d'une tâche avec un titre générique de plus de 5 caractères
        Task(
            title="task",  # Ce titre a plus de 5 caractères mais est générique
            task_type=TaskType.BUGFIX,
            assigned_to=emp,
            project=project,
        )

        # Si aucune exception n'est levée, le test échoue
        print(
            "test_task_title_validation failed: no validation error raised for generic title"
        )
        return False
    except ValueError as e:
        # Vérifie que le message d'erreur est celui attendu
        if "Title must be more descriptive than a generic placeholder" in str(e):
            print(
                "test_task_title_validation passed: validation error correctly raised"
            )
            return True
        else:
            print(f"test_task_title_validation failed: unexpected error message - {e}")
            return False


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


def test_task_with_medium_priority():
    """Test the creation of a Task instance with medium priority."""
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
        title="Review code",
        task_type=TaskType.RESEARCH,
        assigned_to=emp,
        priority=Priority.MEDIUM,
        project=project,
    )
    return True


# ======================================================================
# Execute all tests
# ======================================================================
tests = [
    test_member,
    test_member_with_valid_email,
    test_partner_company,
    test_partner_company_with_invalid_employee_count,
    test_valid_employee,
    test_invalid_name,
    test_invalid_salary,
    test_employee_with_minimum_age,
    test_event_date_validation,
    test_event_invalid_date_validation,
    test_event_with_zero_registered_count,
    test_club,
    test_club_with_empty_lists,
    test_club_with_event_list,
    test_valid_intern,
    test_invalid_education_level,
    test_intern_with_default_department,
    test_project_with_employee,
    test_project_with_intern,
    test_project_with_positive_budget,
    test_project_with_negative_budget,
    test_project_with_string_documentation_link,
    test_valid_task,
    test_task_title_validation,
    test_invalid_title,
    test_invalid_due_date,
    test_invalid_priority_for_documentation,
    test_task_with_medium_priority,
]

all_tests_passed = True
count = 0
for test in tests:
    print(f"\n>>> {test.__name__} 🚀")
    count += 1
    try:
        if test():
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
