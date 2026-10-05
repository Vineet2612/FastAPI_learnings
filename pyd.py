from fastapi import FastAPI  # type: ignore[import-not-found]
from pydantic import BaseModel

app=FastAPI()

class LoaApplication(BaseModel):
    name:str
    age:int
    loan_amount:float
    income:float
    employment_yr:int

@app.post("/predict")
def predict_loan(application:LoaApplication):
    if application.income>50000 and application.employment_yr>2 and application.age>21:
        decision="approved"
    else:
        decision="rejected"

    return {
        "applicant name":application.name,
        "age": application.age,
        "decision": decision}