from pydantic import (
    BaseModel,
    Field,
    HttpUrl,
    field_validator,
    ValidationInfo,
    model_validator,
)
from typing import Optional, List, Union
from datetime import datetime
from enum import Enum


# ======================================================================
# Step 1: Simple class for a Member
#
# This class represents a basic member with an ID, name, and email.
# Attributes:
#   - id: An integer representing the unique identifier for the member.
#   - name: A string representing the name of the member.
#   - email: A string representing the email address of the member.
# ======================================================================
class Member(BaseModel):
    id: int
    name: str
    email: str


# ======================================================================
# Step 2: PartnerCompany class with Field constraints and descriptions
#
# This class represents a partner company with various attributes including
# a website URL, sector, employee count, and active status.
#
# Instructions:
#   - Use Field with descriptions for each attribute.
#   - If no default value is specified, the field is required.
#
# Attributes:
#   - name: A string representing the name of the partner company.
#   - website: An optional HttpUrl representing the official website URL.
#     Optional field
#   - sector: A string representing the business sector of the company.
#   - employee_count: An integer representing the number of employees.
#     Field with a constraint that it must be greater than 0.
#   - is_active: A boolean indicating whether the partnership is active.
#     Field with a default value of True.
# ======================================================================
class PartnerCompany(BaseModel):
    name: str = Field(description="Name of the partner company")
    website: Optional[HttpUrl] = Field(default=None, description="Official website URL")
    sector: str = Field(description="Business sector of the company")
    employee_count: int = Field(gt=0, description="Number of employees (must be > 0)")
    is_active: bool = Field(
        default=True, description="Whether the partnership is active"
    )


# ======================================================================
# Step 3: Employee class with field validators
#
# This class represents an employee with validations on name and salary.
#
# Instructions:
#   - Use Field with descriptions for each attribute.
#   - If no default value is specified, the field is required.
#   - Add validators to enforce business rules.
#
# Attributes:
#   - name: A string representing the name of the employee.
#   - age: An integer representing the age of the employee, must be greater than 18.
#   - salary: A float representing the salary of the employee, defaults to 1400.
# Validators:
#   - name_must_not_contain_digits: Validates that the name does not contain any digits.
#   - salary_must_be_reasonable: Validates that the salary is reasonable based on the employee's age (salary < age * 1000).
# ======================================================================
class Employee(BaseModel):
    name: str = Field(description="Name of the employee")
    age: int = Field(gt=18, description="Age of the employee")
    salary: float = Field(
        default=1400,
        description="Salary of the employee (based arbitrarily on his age)",
    )

    @field_validator("name")
    def name_must_not_contain_digits(cls, v):
        """Validate that the name does not contain any digits."""
        if any(char.isdigit() for char in v):
            raise ValueError("Name must not contain numbers")
        return v

    @field_validator("salary")
    def salary_must_be_reasonable(cls, v, info: ValidationInfo):
        """Validate that the salary is reasonable based on the employee's age."""
        age = info.data.get("age")
        if v < age * 1000:
            raise ValueError("Salary is unrealistically low based on age")
        return v


# ======================================================================
# Step 4: Event class with model validator for date validation
#
# This class represents an event with start and end times, and includes
# validation to ensure the end time is after the start time.
#
# Instructions:
#   - Use Field with descriptions for each attribute.
#   - If no default value is specified, the field is required.
#   - Add validators to enforce business rules.
#
# Attributes:
#   - name: A string representing the name of the event.
#   - registered_count: An integer representing the number of registered attendees, must be greater than or equal to 0.
#   - location: A string representing the location where the event will take place.
#   - start_time: A datetime representing the start time of the event.
#   - end_time: A datetime representing the end time of the event.
# Validators:
#   - check_dates: Validates that the end time is after the start time.
# ======================================================================
class Event(BaseModel):
    name: str = Field(description="Name of the event")
    registered_count: int = Field(ge=0, description="Number of registered attendees")
    location: str = Field(description="Location where the event will take place")
    start_time: datetime = Field(description="Start time of the event")
    end_time: datetime = Field(description="End time of the event")

    @model_validator(mode="before")
    def check_dates(cls, values):
        """Validate that the end time is after the start time."""
        start = values.get("start_time")
        end = values.get("end_time")
        if end <= start:
            raise ValueError("End time must be after start time")
        return values


# ======================================================================
# Step 5: Club class with object relationships
#
# This class represents a club with members, partner companies, and events.
#
# Instructions:
#   - Use Field with descriptions for each attribute.
#   - If no default value is specified, the field is required.
#
# Attributes:
#   - name: A string representing the name of the club.
#   - members: A list of Member objects representing the list of club members, defaults to an empty list.
#   - partner_companies: A list of PartnerCompany objects representing the list of partner companies, defaults to an empty list.
#   - events: An optional list of Event objects representing the list of club events, defaults to None.
# ======================================================================
class Club(BaseModel):
    name: str = Field(description="Name of the club")
    members: List[Member] = Field(
        default_factory=list, description="List of club members"
    )
    partner_companies: List[PartnerCompany] = Field(
        default_factory=list, description="List of partner companies"
    )
    events: Optional[List[Event]] = Field(
        default=None, description="List of club events"
    )


# ======================================================================
# Step 6: Inter class with Enums for EducationLevel and Department
#
# This section defines enumerations used to standardize the representation
# of education levels and departments within the application.
#
# Instructions:
#   - Use Field with descriptions for each attribute.
#   - If no default value is specified, the field is required.
#   - Use enums to restrict fields to a predefined set of valid values.
#
# Enumerations:
#   - EducationLevel: Represents different levels of education that an intern
#       might have attained (BACHELOR, MASTER, PHD, HIGH_SCHOOL).
#       This helps in categorizing and validating the education level of individuals.
#   - Department: Represents different departments within an organization
#       (AI, DATA, COM, HR). This helps in categorizing and assigning individuals
#       to specific departments.
#
# Attributes:
#   - name: A string representing the name of the intern.
#   - age: An integer representing the age of the employee, must be greater than 16.
#   - education_level: An EducationLevel enum representing the education level of the intern.
#   - department: A Department enum representing the department to which the intern is assigned.
#                 This field defaults to the Data Science department.
# ======================================================================
class EducationLevel(Enum):
    BACHELOR = "bachelor"
    MASTER = "master"
    PHD = "phd"
    HIGH_SCHOOL = "high_school"


class Department(Enum):
    AI = "Artificial Intelligence"
    DATA = "Data Science"
    COM = "Software Development"
    HR = "Human Resources"


class Intern(BaseModel):
    name: str = Field(description="Name of the intern")
    age: int = Field(gt=16, description="Age of the intern")
    education_level: EducationLevel = Field(description="Education level of the intern")
    department: Department = Field(
        default=Department.DATA, description="Assigned department"
    )


# ======================================================================
# Step 7: Project class using Union
#
# This class represents a project with various attributes including a name,
# client, assigned person, deadline, budget, and documentation link.
#
# Instructions:
#   - Use Field with descriptions for each attribute.
#   - If no default value is specified, the field is required.
#
# Attributes:
#   - name: A string representing the name of the project.
#   - client: A string representing the client associated with the project.
#   - assigned_to: A union type that can either be an Employee or an Intern,
#       representing the person to whom the project is assigned.
#   - deadline: An optional datetime object representing the deadline for the project.
#       This field is optional and defaults to None.
#   - budget_euros: An optional float representing the budget in euros.
#       This field must be positive if provided and defaults to None.
#   - documentation_link: A union type that can either be a URL (HttpUrl) or a string,
#       representing a link or internal reference to the project documentation.
#
# ======================================================================
class Project(BaseModel):
    name: str = Field(description="Name of the project")
    client: str = Field(description="Client associated with the project")
    assigned_to: Union[Employee, Intern] = Field(
        description="Person assigned to the project"
    )
    deadline: Optional[datetime] = Field(
        default=None, description="Deadline of the project"
    )
    budget_euros: Optional[float] = Field(
        default=None, gt=0, description="Optional budget in euros (must be positive)"
    )
    documentation_link: Union[HttpUrl, str] = Field(
        description="URL or internal reference to documentation"
    )


# ======================================================================
# Step 8: Task class combining various Pydantic features
#
# This class represents a task with a title, type, assigned person, priority,
# due date, completion status, and associated project.
#
# Instructions:
#   - Use Field with descriptions for each attribute.
#   - If no default value is specified, the field is required.
#   - Add validators to enforce business rules.
#   - Use enums to restrict fields to a predefined set of valid values.
#
# Enumerations:
#   - Priority: Represents different priority levels of a task (LOW, MEDIUM, HIGH).
#     This helps in categorizing and managing the priority of tasks.
#   - TaskType: Represents different types of tasks (FEATURE, BUGFIX, DOCUMENTATION, RESEARCH).
#     This helps in categorizing and assigning tasks based on their type.
#
# Attributes:
#   - title: A string representing the title of the task. It must be at least
#     5 characters long to ensure it is descriptive enough.
#   - task_type: A TaskType enumeration representing the type of task.
#   - assigned_to: A union type that can either be an Employee or an Intern,
#     representing the person to whom the task is assigned.
#   - priority: A Priority enumeration representing the priority of the task, defaulting to MEDIUM.
#   - due_date: An optional datetime object representing the deadline for the task, defaulting to None.
#   - is_completed: A boolean indicating whether the task is completed, defaulting to False.
#   - project: A Project object representing the project to which this task belongs.
#
# Validators:
#   - title_must_not_be_generic: Ensures that the task title is descriptive
#     and not a generic placeholder ('task', 'todo', 'fix').
#   - validate_due_date_and_priority: Ensures that the due date is not in the past
#     and that DOCUMENTATION tasks do not have HIGH priority.
# ======================================================================
class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class TaskType(str, Enum):
    FEATURE = "feature"
    BUGFIX = "bugfix"
    DOCUMENTATION = "documentation"
    RESEARCH = "research"


class Task(BaseModel):
    title: str = Field(min_length=5, description="Title must be descriptive enough")
    task_type: TaskType = Field(description="Type of the task")
    assigned_to: Union[Employee, Intern] = Field(
        description="Person assigned to the task"
    )
    priority: Priority = Field(default=Priority.MEDIUM)
    due_date: Optional[datetime] = Field(default=None, description="Task deadline")
    is_completed: bool = Field(default=False)
    project: Project = Field(description="The project to which this task belongs")

    @field_validator("title")
    def title_must_not_be_generic(cls, v):
        """Validates that the task title is descriptive and not a generic placeholder."""
        if v.lower() in ["task", "todo", "fix"]:
            raise ValueError(
                "Title must be more descriptive than a generic placeholder."
            )
        return v

    @model_validator(mode="after")
    def validate_due_date_and_priority(self):
        """Validates the due date and priority logic of the task."""
        if self.due_date and self.due_date < datetime.now():
            raise ValueError("Due date cannot be in the past.")
        if self.priority == Priority.HIGH and self.task_type == TaskType.DOCUMENTATION:
            raise ValueError("Documentation tasks should not have high priority.")
        return self
