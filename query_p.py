from fastapi import FastAPI

app = FastAPI()

cutomer_risk_profiles={
    101:{"name":"Raj Sharma","city":"Mumbai","risk":"low","risk_score":0.2},
    102:{"name":"Rakesh","city":"Delhi","risk":"medium","risk_score":0.5},
    103:{"name":"ARAV","city":"Bangalore","risk":"high","risk_score":0.8},
    104:{"name":"Arjun Kapoor","city":"Delhi","risk":"high","risk_score":0.1},
    105:{"name":"Asif","city":"Bangalore","risk":"medium","risk_score":0.59},
}

@app.get("/customers")
def get_customers(city:str,risk:str| None=None):
    filtered=[
        c for c in cutomer_risk_profiles.values() 
        if c["city"].lower()==city.lower() and (risk is None or c["risk"].lower()==risk.lower())
    ]
    return {
        "city":city,
        "risk":risk,
        "count":len(filtered),
        "results":filtered
    }