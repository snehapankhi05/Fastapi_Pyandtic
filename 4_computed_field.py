from pydantic import BaseModel , EmailStr , computed_field
from typing import List, Dict  

class Patient(BaseModel):

    name:str
    email : EmailStr
    age : int
    weight : float
    height : float
    married : bool
    allergies : list[str]
    contact_details : dict[str,str] 

    @computed_field
    @property
    def bmi(self) -> float:
        height_in_m = self.height / 100   # cm → meter
        bmi = round(self.weight / (height_in_m ** 2), 2)
        return bmi
    
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
    print('BMI',patient.bmi)
    print('updated')

patient_info = {'name':'sneha',
                'email':'abc@hdfc.com',
                'age':20,
                'weight':55.5,
                'height':165.0,
                'married':False,
                'allergies':['pollen','dust'], 
                'contact_details':{'phone':'1234567890','emergency':'0987654321'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1) 