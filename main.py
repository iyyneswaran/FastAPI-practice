from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/')
def run_check():
    return {"message": "API is running"}

@app.get('/greet/{name}')
def greet(name: str, age: Optional[int] = None):
    if age is not None:
        return {
            "message": f"Hello, {name}! You are {age} years old."
        }
    
    return {
        "message": f"Hello, {name}!"
    }