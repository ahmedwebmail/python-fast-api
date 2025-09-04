from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: int

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/add-user")
def create_user(user: User):
    return {"got": user}