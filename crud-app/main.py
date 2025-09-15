from fastapi import FastAPI, Depends, HTTPException
import models, schemas,crud
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from typing import List

Base.metadata.create_all(bind = engine)

app = FastAPI()

#Dependency with the DB
# when user hits a route, api access the DB and fetch or store something from/in the DB
# so there is some dependency of DB on API, so we create a Dependency function which gives a DB session and after completing the task, it closes the DB session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1st endpoint
# creating an employee
@app.post('/emplyoee',response_model=schemas.EmployeeOut)
def create_employee(employee: schemas.EmployeeCreate, db : Session = Depends(get_db)):
    return crud.create_employee(db,employee)

#2. get all employess
@app.get('/employee', response_model= List[schemas.EmployeeOut])
def get_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)

#3. get specific employee
@app.get('/employee/{emp_id}', response_model = schemas.EmployeeOut)
def get_employee(emp_id: int, db : Session = Depends(get_db)):
    employee = crud.get_employee(db,emp_id)
    
    if employee:
        return employee
    else:
        raise HTTPException(status_code=404, detail='Employee not found')


#4. update an employee
@app.put('/employee/{emp_id}', response_model=schemas.EmployeeOut)
def update_employee(emp_id : int, employee: schemas.EmployeeUpdate, db : Session = Depends(get_db)):
    db_emp = crud.update_employee(db,emp_id,employee)
    
    if db_emp:
        return employee
    else:
        raise HTTPException(status_code=404, detail='Employee not found')
    
#5. delete an employee
@app.delete("/employee/{emp_id}" , response_model= dict)
def delete_emp(emp_id : int, db : Session = Depends(get_db)):
    emp = crud.delete_employee(db,emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="employee not found")
    return {"message" : "Employee succesfully deleted"}    