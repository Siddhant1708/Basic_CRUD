from fastapi import FastAPI, HTTPException
from typing import List
from models import Employee

app = FastAPI()


Employes: List[Employee] = []

@app.get('/')
def get_():
    return {"message": "Hello"}

@app.get('/emp', response_model=List[Employee])
def get_employees():
    return Employes

@app.get('/emp/{id}', response_model=Employee)
def get_emp(id : int):
    for ind, emp in enumerate(Employes):
        if emp.id == id:
            return Employes[ind]
    raise HTTPException(status_code=404, detail="Emplyoee not found")

@app.post('/emp',response_model=Employes)
def add_emp(new_emp : Employee):
    for emp in Employes:
        if emp.id == new_emp:
            raise HTTPException(status_code=400, detail="Employee already found")
    Employes.append(new_emp)
    return new_emp

@app.delete('/emp/{id}')
def del_emp(id : int):
    for ind, emp in enumerate(Employes):
        if emp.id == id:
            del Employes[ind]
            return {"message": "Employee deleted"}
    raise HTTPException(status_code=404, detail="Employee not found")   
    

@app.put('/emp/{id}', response_model=Employee)
def update(id : int, emp : Employee):
    for ind, emps in enumerate(Employes):
        if emps.id == id:
            Employes[ind] = emp
            return Employes[ind]
    raise HTTPException(status_code=404, detail="Employee not found")       