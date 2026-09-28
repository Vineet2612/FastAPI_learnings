from fastapi import FastAPI  # type: ignore[reportMissingImports]
app=FastAPI()
@app.get("/")
def home():
    return{"message":"my firstAPI is working" }

@app.get("/about")
def about():
    return{"project":"loan risk model","version":"1.00.0" }

@app.get("/customer")
def customer(customer_id:int):
    return {
        "customer_id":customer_id,
        "name":"Ravi",
        "status":"active"
    }
