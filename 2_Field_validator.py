from pydantic import BaseModel , EmailStr, AnyUrl, Field , field_validator
from typing import List, Dict , Optional , Annotated

class Patient(BaseModel):

    name:str
    email : EmailStr
    age : int
    weight : float
    married : bool
    allergies : list[str]
    contact_details : dict[str,str] 

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):

        valid_domains = ['hdfc.com','icici.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value

    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('inserted')

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated')

patient_info = {'name':'sneha',
                'email':'abc@hdfc.com',
                'age':20,
                'weight':55.5,
                'married':False,
                'allergies':['pollen','dust'], 
                'contact_details':{'phone':'1234567890'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1) 