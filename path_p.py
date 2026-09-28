from fastapi import FastAPI

app = FastAPI()
cutomer_risk_profiles={
    101:{"name":"Raj Sharma","risk":"low","risk_score":0.2},
    102:{"name":"Aakash Singh","risk":"medium","risk_score":0.5},
    103:{"name":"Arjun Kapoor","risk":"high","risk_score":0.8},
}

@app.get("/customer/{customer_id}")
def get_customer_risk_profile(customer_id:int):
    if customer_id not in cutomer_risk_profiles:
        return {"error": f"Customer {customer_id} not found"}
    profile = cutomer_risk_profiles[customer_id]
    return {"customer_id":customer_id,"name":profile["name"],"risk":profile["risk"],"risk_score":profile["risk_score"]}

@app.get("/model/{model_name}/customer/{customer_id}")
def get_customer_risk_profile_with_model(model_name:str,customer_id:int):
    if customer_id not in cutomer_risk_profiles:
        return {"error": f"Customer {customer_id} not found"}
    profile = cutomer_risk_profiles[customer_id]
    return {"model_name":model_name,"customer_id":customer_id,"name":profile["name"],"risk":profile["risk"],"risk_score":profile["risk_score"]}