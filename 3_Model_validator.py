from pydantic import BaseModel , EmailStr, AnyUrl, Field , field_validator , model_validator
from typing import List, Dict , Optional , Annotated

class Patient(BaseModel):

    name:str
    email : EmailStr
    age : int
    weight : float
    married : bool
    allergies : list[str]
    contact_details : dict[str,str] 

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Emergency contact is required for patients above 60 years')
        return model
    
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
                'contact_details':{'phone':'1234567890','emergency':'0987654321'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1) 