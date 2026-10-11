# def insert_patient_data():
#     # not an actual code , but a depiction for understanding the need of Pydantic
#     print(name)
#     print(age)
#     print('inserted patient data into the database...')

# insert_patient_data('Hi','Hello')
# """
# No type validation is done here, so if we pass an integer instead of a string for name or age, it will still work and insert the data into the database. This can lead to unexpected behavior and errors in the application.
# """

# def insert_patient_data2(name:str, age:int):
#     # not an actual code , but a depiction for understanding the need of Pydantic
#     print(name)
#     print(age)
#     print('inserted patient data into the database...')

# insert_patient_data2('Hi',32)
# """A soln is do the above thing , but still there is no validation done for the data types, so if we pass an integer instead of a string for name or age. Python's type forcing is not that strict, so it will still work and insert the data into the database."""

# # -> we arent able to enforce the data types 


# def insert_patient_data3(name:str, age:int):
#     # not an actual code , but a depiction for understanding the need of Pydantic
#     if type(name) != str:
#         raise ValueError('Name must be a string')
#     if type(age) != int:
#         raise ValueError('Age must be an integer')  
#     print(name)
#     print(age)
#     print('inserted patient data into the database...')
# But still we are not able to enforce the data types in a clean way, and we have to write a lot of code for validation. 

# 1) Type validation is the 1st problem
# 2) Data validation is the 2nd problem, for example if we want to validate that the age should be between 0 and 120, we have to write a lot of code for that as well.

# -------------------------------------------SOLVE THE PROBLEM---------------------------------------------
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'])]
    # email: EmailStr
    #linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    #weight: Annotated[float, Field(gt=0, strict=True)]
    #married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
    #allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    # contact_details: Dict[str, str] 

def insert_patient_data4(patient: Patient):
    print(patient.name)
    print(patient.age)

patient_data = {
    "name": "Nitish",
    "age": 25
}

patient = Patient(**patient_data)
insert_patient_data4(patient)











