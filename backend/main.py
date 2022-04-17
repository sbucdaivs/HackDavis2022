from health_model import ML_Model

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Profile(BaseModel):
    bp_systolic: int
    bp_diastolic: int
    heart_rate: int
    age: int
    body_temp: int
    blood_sugar: float

class Contact(BaseModel):
    phone_number: str
    first_name: str
    last_name: str

model_instance = None

@app.on_event("startup")
async def startup_event():
    global model_instance
    model_instance = ML_Model()
    model_instance.train_model()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/get_risk")
async def get_risk(profile: Profile):
    data_list = np.array([profile.age, profile.bp_systolic, profile.bp_diastolic, profile.blood_sugar, profile.body_temp, profile.heart_rate]).reshape(1, -1)
    pred = model_instance.predict(data_list)
    print(pred)
    risk_level = "unknown"
    if pred == 0:
        risk_level = "low"
    if pred == 1:
        risk_level = "medium"
    if pred == 2:
        risk_level = "high"
    return {"risk_level": risk_level}

@app.post("/notify_signup")
async def notify_signup(contact: Contact):
    return {"status": "ok"}
