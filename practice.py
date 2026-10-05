from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# -----------------------------
# Pydantic Model
# -----------------------------

class HealthInsuranceApplication(BaseModel):
    name: str
    age: int
    sex: str
    BMI: float
    number_of_children: int
    smoker: bool


# -----------------------------
# Temporary Database
# -----------------------------

customers = {}


# -----------------------------
# GET
# -----------------------------

@app.get("/")
def home():
    return {
        "message": "Welcome to Health Insurance API"
    }


# -----------------------------
# GET + Path Parameter
# -----------------------------

@app.get("/customer/{customer_id}")
def get_customer(customer_id: int):

    if customer_id not in customers:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return {
        "customer_id": customer_id,
        "customer": customers[customer_id]
    }


# -----------------------------
# GET + Query Parameter
# -----------------------------

@app.get("/customers")
def get_customers(smoker: bool | None = None):

    if smoker is None:
        return {
            "customers": customers
        }

    filtered_customers = {
        customer_id: customer
        for customer_id, customer in customers.items()
        if customer["smoker"] == smoker
    }

    return {
        "smoker": smoker,
        "customers": filtered_customers
    }


# -----------------------------
# POST
# Predict Insurance Charge
# -----------------------------

@app.post("/predict")
def predict_health_insurance(
    application: HealthInsuranceApplication
):

    base = 20000

    # Age
    if application.age < 25:
        base = base

    elif application.age <= 40:
        base = base + 5000

    elif application.age <= 60:
        base = base + 12000

    else:
        base = base + 20000


    # BMI
    if application.BMI < 18.5:
        base = base + 2000

    elif application.BMI < 25:
        base = base

    elif application.BMI < 30:
        base = base + 5000

    else:
        base = base + 15000


    # Smoking
    if application.smoker:
        base = base + 30000


    # Number of children
    if application.number_of_children == 0:
        base = base

    elif application.number_of_children <= 2:
        base = base + 3000

    else:
        base = base + 6000


    # Sex
    if application.sex.lower() == "male":
        base = base + 2000


    return {
        "name": application.name,
        "age": application.age,
        "predicted_insurance_charge": base
    }


# -----------------------------
# POST
# Create Customer
# -----------------------------

@app.post("/customer/{customer_id}")
def create_customer(
    customer_id: int,
    application: HealthInsuranceApplication
):

    if customer_id in customers:
        raise HTTPException(
            status_code=400,
            detail="Customer already exists"
        )

    customers[customer_id] = application.model_dump()

    return {
        "message": "Customer created successfully",
        "customer_id": customer_id,
        "customer": customers[customer_id]
    }


# -----------------------------
# PUT
# Update Customer
# -----------------------------

@app.put("/customer/{customer_id}")
def update_customer(
    customer_id: int,
    application: HealthInsuranceApplication
):

    if customer_id not in customers:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    customers[customer_id] = application.model_dump()

    return {
        "message": "Customer updated successfully",
        "customer_id": customer_id,
        "customer": customers[customer_id]
    }


# -----------------------------
# DELETE
# -----------------------------

@app.delete("/customer/{customer_id}")
def delete_customer(customer_id: int):

    if customer_id not in customers:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    deleted_customer = customers.pop(customer_id)

    return {
        "message": "Customer deleted successfully",
        "customer_id": customer_id,
        "deleted_customer": deleted_customer
    }