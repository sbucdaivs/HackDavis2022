from ast import Str
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

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

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/get_risk")
async def get_risk(profile: Profile):
    return {"risk_level": "low"}

@app.post("/notify_signup")
async def notify_signup(contact: Contact):
    return {"status": "ok"}
