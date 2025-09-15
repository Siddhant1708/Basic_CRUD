from sqlalchemy.orm import Session
import models, schemas

def get_employees(db : Session):
    return db.query(models.Employee).all()


def get_employee(db: Session, emp_id : int):
    return db.query(models.Employee).filter(models.Employee.id == emp_id).first()


def create_employee(db : Session, emp : schemas.EmployeeCreate):
    db_employee = models.Employee(
        name = emp.name,
        email = emp.email
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee) # through this emp will get an id, since we are not giving any id explicitly (because id is an autogenrated field)

def update_employee(db : Session, emp_id : int, employee : schemas.EmployeeUpdate):
    db_employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if db_employee:
        db_employee.name = employee.name
        db_employee.email = employee.email
        db.commit()
        db.refresh(db_employee)
    return db_employee


def delete_employee(db : Session, emp_id : int):
    db_employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee    
