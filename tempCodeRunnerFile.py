from pydantic import BaseModel , EmailStr
from typing import List, Dict , Optional

class Patient(BaseModel):
    name : str
    email : EmailStr
    age : int
    weight : float = 0.0
    married : Optional[bool]=None
    allergies : list[str]
    contact_details : dict[str,str]

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
                'email':'abc@gmail.com',
                'age':20,
                'weight':55.5,
                'married':False,
                'allergies':['pollen','dust'], 
                'contact_details':{'phone':'1234567890'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)