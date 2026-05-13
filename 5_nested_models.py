from pydantic import BaseModel 

class Address(BaseModel):

    city : str
    state : str
    pin : str

class Patient(BaseModel):

    name : str
    gender : str
    age : int
    address : Address

address_dic = {'city':'Mumbai',
               'state':'Maharashtra',
               'pin':'400001'}

address1=Address(**address_dic)

patient_dict= {'name':'Sneha','gender':'Female','age':25,'address':address1}

patient1=Patient(**patient_dict)

print(patient1)
print(patient1.address.city)

# Better organization of related data using nested models (eg: vitals , address , insurance etc.,)

# Reusability of models across different parent models

# Improved readability and maintainability of code

# Readability of complex data structures and easier for developers and API conumsers to understand

# Validation: Nested models are validated automatically-no extra effort needed