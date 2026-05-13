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

temp=patient1.model_dump(include=['name','address'])
print(temp)
print(type(temp))

temp2=patient1.model_dump_json(exclude={'address':{'pin'} })
print(temp2)
print(type(temp2))