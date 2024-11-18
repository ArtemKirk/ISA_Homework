from fastapi import FastAPI
from random import random
from pydantic import BaseModel

app = FastAPI()

class ScoreRequest(BaseModel):
    login: str


@app.post("/score/")
def score(score_request: ScoreRequest):
    login = score_request.login
    
    try:
        score = random()
        return {'login': login, 'score': score}
    except:
        return {'login': login, 'score': 1.0}
