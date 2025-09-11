from pydantic import BaseModel, Field, StrictInt
from typing import Optional


class Employee(BaseModel):
    id : int = Field(...,gt=0)   #using ... this field becomes mandatory and gt == greater than
    name: str = Field(..., min_length=3)
    department : str = Field(..., min_length=3, max_length=20)
    age : Optional[StrictInt] = Field(default=None)  # using Optional, age becomes optional, but when we use Field(default=None), if user does not provide any value , it becomes none
