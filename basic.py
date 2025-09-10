from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class nums(BaseModel):
    num1: int
    num2: int

class out(BaseModel):
    sum: int



@app.post('/', response_model=out)
def add(numsi : nums):
    
    return out(sum = numsi.num1 + numsi.num2)
