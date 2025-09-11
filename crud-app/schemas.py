from pydantic import BaseModel, EmailStr


class EmployeeBase(BaseModel):
    name : str
    email : EmailStr


class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class EmployeeOut(EmployeeBase):
    id : int

    class Config:
        orm_mode = True  # at the time of reading employee data from the DB, it helps to parse data from the DB