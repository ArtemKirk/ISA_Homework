from fastapi import FastAPI
from pydantic import BaseModel

users = {
    'user1': 'qwerty',
    'user2': '12345',
    'admin': 'admin',
}

app = FastAPI()

class AuthRequest(BaseModel):
    login: str
    password: str

@app.post("/auth/")
def auth(auth_request: AuthRequest):
    login = auth_request.login
    password = auth_request.password
    
    if login in users and users[login] == password:
        return {"login": login, "authenticated": True}
    else:
        return {"login": login, "authenticated": False}