from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()

class User(BaseModel):
    username: str = Field(..., min_length=3)
    email: EmailStr
    age: int = Field(..., gt=18)

@app.post("/register")
def register_user(user: User):

    return {
        "message": "User registered successfully",
        "user": user
    }