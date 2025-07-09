# Pydantic Exercise : Progressive Model Development

This exercise is structured into four stages, each building upon the previous one. You will work within fives directories: `model_1`, `model_2`, `model_3`, `model_4` and `structured_output`. In each stage, you will extend the functionality of the existing code by adding new features and exploring important aspects of Pydantic. The final stage, `structured_output`, introduces how Pydantic can be combined with an AI system to generate and validate structured responses. Follow the instructions for each stage and modify the classes in their respective files accordingly.


## Stage 1 : Foundational Classes - [folder model_1](src/workshop_pydantic/model_1)

In this stage, you will create the basic structure of the classes, setting up the foundational models that will be extended in subsequent stages. This involves defining the primary attributes for each class without additional constraints or validations.

### File : [people.py](src/workshop_pydantic/model_1/people.py)

1. **Create the `Person` class**
   - Define a class named `Person` with attributes `name` and `email`, both of which are strings.

2. **Create the `Member` class**
   - Define a class named `Member` that inherits from `Person`. Add attributes `id` (integer) and `company` (PartnerCompany).

3. **Create the `Freelancer` class**
   - Define a class named `Freelancer` that inherits from `Person`. Add attributes `id` (integer), `specialty` (string), `companies` (list of PartnerCompany or Company), and `daily_rate` (optional integer).

4. **Create the `Researcher` class**
   - Define a class named `Researcher` that inherits from `Person`. Add attributes `id` (integer), `field_of_study` (string), and `number_of_articles` (integer).

### File : [company.py](src/workshop_pydantic/model_1/company.py)

5. **Create the `Company` class**
   - Define a class named `Company` with attributes `name` (string), `website` (optional HttpUrl), `sector` (string), and `employee_count` (integer).

6. **Create the `PartnerCompany` class**
   - Define a class named `PartnerCompany` that inherits from `Company`. Add an attribute `is_active` which is a boolean.

### File : [event.py](src/workshop_pydantic/model_1/event.py)

7. **Create the `Event` class**
   - Define a class named `Event` with attributes `name` (string),`event_type` (string), `registrants` (list of Member, Freelancer, or Researcher), `location` (string), `start_time` (datetime), and `end_time` (datetime).
   - Add a computed field `register_count` that returns the number of registrants.

### File : [club.py](src/workshop_pydantic/model_1/club.py)

8. **Create the `Club` class**
   - Define a class named `Club` with attributes `members` (list of Member, Freelancer, or Researcher), `partner_companies` (list of PartnerCompany), and `events` (list of Event).


## Stage 2 : Incorporating Enums - [folder model_2](src/workshop_pydantic/model_2)

In this stage, you will add enumerations to define specific sets of values for certain fields. You will modify the existing classes to use these enums, enhancing the structure and type safety of the models.

### File : [enums.py](src/workshop_pydantic/model_2/enums.py)

1. **Create the `Sector` enum**
   - Define an enum named `Sector` with the following values: `TECHNOLOGY`, `HEALTHCARE`, `EDUCATION`, and `FINANCE`.

2. **Create the `Specialty` enum**
   - Define an enum named `Specialty` with the following values: `SOFTWARE_DEVELOPMENT`, `DATA_SCIENCE`, `CYBERSECURITY`, and `DEVOPS`.

3. **Create the `FieldOfStudy` enum**
   - Define an enum named `FieldOfStudy` with the following values: `COMPUTER_SCIENCE`, `BIOLOGY`, `PHYSICS`, and `CHEMISTRY`.

4. **Create the `EventType` enum**
   - Define an enum named `EventType` with the following values: `WORKSHOP`, `CONFERENCE`, `SEMINAR`, and `DATATHON`.

### File : [company.py](src/workshop_pydantic/model_2/company.py)

5. **Modify the `Company` class**
   - Update the `sector` attribute to use the `Sector` enum.

### File : [people.py](src/workshop_pydantic/model_2/people.py)

6. **Modify the `Freelancer` class**
   - Update the `specialty` attribute to use the `Specialty` enum.

7. **Modify the `Researcher` class**
   - Update the `field_of_study` attribute to use the `FieldOfStudy` enum.

### File : [event.py](src/workshop_pydantic/model_2/event.py)

8. **Modify the `Event` class**
   - Update the `event_type` attribute to use the `EventType` enum.

By incorporating these enums, you will ensure that certain fields in your models can only take predefined values, thereby increasing the robustness and clarity of your code.

## Stage 3 : Adding Field Validations - [folder model_3](src/workshop_pydantic/model_3)

In this stage, you will enhance the existing classes by adding field validations and descriptions. This will ensure that the data adheres to specific constraints and provide clarity on the expected data format.

### File : [people.py](src/workshop_pydantic/model_3/people.py)

1. **Modify the `Person` class**
   - Add field validations and descriptions for the `name` and `email` attributes.
   - `name`: Ensure it has a minimum length of 2 and a maximum length of 50.
   - `email`: Add a regex pattern to validate the email format (`r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"`).

2. **Modify the `Member` class**
   - Add field validations and descriptions for the `id` and `company` attributes.
   - `id`: Ensure it is greater than 0.

3. **Modify the `Freelancer` class**
   - Add field validations and descriptions for the `id`, `specialty`, `companies`, and `daily_rate` attributes.
   - `id`: Ensure it is greater than 0.
   - `companies`: initialize as an empty list.
   - `daily_rate`: Ensure it is greater than 0, a multiple of 50, and does not allow infinite or NaN values.

4. **Modify the `Researcher` class**
   - Add field validations and descriptions for the `id`, `field_of_study`, and `number_of_articles` attributes.
   - `id`: Ensure it is greater than 0.
   - `number_of_articles`: Ensure it is greater than or equal to 0, with a default value of 0, and does not allow infinite or NaN values.

### File : [company.py](src/workshop_pydantic/model_3/company.py)

5. **Modify the `Company` class**
   - Add field validations and descriptions for the `name`, `website`, `sector`, and `employee_count` attributes.
   - `name`: Ensure it has a minimum length of 2 and a maximum length of 100.
   - `website`: Provide a default value of `None`.
   - `employee_count`: Ensure it is greater than 0 and less than 100,000.

6. **Modify the `PartnerCompany` class**
   - Add field validations and descriptions for the `is_active` attribute.
   - `is_active`: Provide a default value of `True`.

### File : [event.py](src/workshop_pydantic/model_3/event.py)

7. **Modify the `Event` class**
   - Add field validations and descriptions for the `event_type`, `registrants`, `location`, `start_time`, and `end_time` attributes.
   - `registrants`: initialize as an empty list.
   - `location`: Ensure it has a minimum length of 2 and a maximum length of 200.

### File : [club.py](src/workshop_pydantic/model_3/club.py)

8. **Modify the `Club` class**
   - Add field validations and descriptions for the `name`, `members`, `partner_companies`, and `events` attributes.
   - `name`: Ensure it has a minimum length of 2 and a maximum length of 100.
   - For `members`, `partner_companies`, and `events` to initialize them as empty lists.

By adding these field validations and descriptions, you will ensure that the data in your models is well-defined and adheres to specific constraints, improving the robustness and clarity of your code.

## Stage 4 : Adding Custom Validators - [folder model_4](src/workshop_pydantic/model_4)

In this stage, you will enhance the existing classes by adding custom validators. These validators will enforce specific business rules and constraints, ensuring that the data adheres to more complex conditions.

### File : [people.py](src/workshop_pydantic/model_4/people.py)

1. **Modify the `Person` class**
   - Add a field validator for the `name` attribute to ensure it does not contain special characters or numbers (you can use *.isalpha()* for example)

2. **Modify the `Freelancer` class**
   - Add a field validator for the `daily_rate` attribute to enforce minimum daily rates based on the freelancer's specialty (so use *ValidationInfo*):
     - Software Development: at least 300 euros
     - Data Science: at least 350 euros
     - Cybersecurity: at least 400 euros
     - DevOps: at least 375 euros

### File : [company.py](src/workshop_pydantic/model_4/company.py)

3. **Modify the `Company` class**
   - Add a field validator for the `website` attribute to ensure that companies in the finance sector must have a website.

### File : [event.py](src/workshop_pydantic/model_4/event.py)

4. **Modify the `Event` class**
   - Add a model validator (mode="before") to ensure that the `start_time` is before the `end_time`.
   - Add a model validator (mode="after") to enforce specific rules for events:
     - Datathon events must have at least 10 registered attendees.
     - Non-networking events must have at least one registrant.

### File : [club.py](src/workshop_pydantic/model_4/club.py)

5. **Modify the `Club` class**
   - Add a field validator for the `events` attribute to ensure that clubs with more than 100 members must have at least 3 events (use *ValidationInfo*).
   - Add a model validator (mode="before") to ensure that a club must have at least one member, partner company, or event.

By adding these custom validators, you will ensure that the data in your models adheres to specific business rules and constraints, improving the robustness and reliability of your code.

## Stage 5: Structured Output with AI Integration - [folder structured_output](src/workshop_pydantic/structured_output)

In this final stage, you will integrate Pydantic with an AI system to generate and validate structured responses. This involves using the OpenAI API to create instances of your models based on AI-generated content.

Don’t forget to add your API key in the `.env` file, and then fill in the `...` placeholders in the script accordingly.

### File : [generate_club.py](src/workshop_pydantic/structured_output/generate_club.py)

### Configure the OpenAI Client

- Use `load_dotenv` to load environment variables from a `.env` file.
- Initialize the OpenAI client.

### Use the OpenAI API to Generate Club Information

- Use the `client.beta.chat.completions.parse` method to generate structured club information.
- Specify the model to be used, such as "gpt-4o-mini".
- Define the messages for the API. To effectively communicate with the AI, you need to define the messages you send to it. This includes a system message that sets the context or role of the AI, such as being a helpful assistant that generates club information. Additionally, you should include a user message that clearly outlines the task, such as generating detailed information about a club
- Use the `Club` model as the response format to structure the generated data.

### Convert and Save the Results

- Convert the generated result into a dictionary using `json.loads`.
- Save the dictionary into a JSON file named `club.json` with proper indentation for readability.

>Combining Pydantic with AI models ensures structured, validated, and tailored data generation, enhancing application efficiency and reliability.

---

With the completion of these stages, you have successfully built and refined a comprehensive set of models using Pydantic, ensuring structured and validated data generation that enhances the efficiency and reliability of your applications !
