from fastapi import FastAPI
import requests
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv() 

THRESHOLD = float(os.getenv("SCORE_THRESHOLD", 0.5))

app = FastAPI()

class CompositionRequest(BaseModel):
    login: str
    password: str


@app.post("/composition/")
def composition(composition_request: CompositionRequest):
    login = composition_request.login
    password = composition_request.password

    try:
        score_request = requests.post("http://127.0.0.1:8001/score/", json=({'login': login}))
        score = score_request.json()['score']
    except:
        score = 1

    if score < THRESHOLD:
        return {"login": login, "authenticated": False}
    
    try:
        auth_request = requests.post("http://127.0.0.1:8002/auth/", json=({'login': login, 'password': password}))
        auth = auth_request.json()['authenticated']
    except:
        auth = False

    if auth:
        return {"login": login, "authenticated": True}
        
    return {"login": login, "authenticated": False}
