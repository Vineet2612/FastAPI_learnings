from fastapi import FastAPI  
from pydantic import BaseModel

app=FastAPI()
class LoaApplication(BaseModel):
    age:int
    loan_amount:float
    income:float
    employment_yr:int

@app.get("/")
def home():
    return {"message": "Loan Prediction API is running"}

@app.post("/predict")
def predict_loan(application:LoaApplication):

    #pretending this is trained model
    if application.income>50000 and application.employment_yr>5:
        decision="approved"
    else:
        decision="rejected"

    return {
        "age": application.age,
        "decision": decision}