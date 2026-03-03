from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def greeting():
    return {
        "message": "Welcome to the simple calculator API!"
    }

@app.get("/add")
def addition(a: float, b: float):
    result = a + b
    return {
        "operation": "addition",
        "operands": [a, b],
        "result": result
    }

@app.get("/subtract")
def subtraction(a: float, b: float):
    result = a - b
    return {
        "operation": "subtraction",
        "operands": [a, b],
        "result": result
    }

@app.get("/multiply")
def multiplication(a: float, b: float):
    result = a * b
    return {
        "operation": "multiplication",
        "operands": [a, b],
        "result": result
    }

@app.get("/divide")
def division(a: float, b: float):
    if b == 0:
        return {
            "error": "Division by zero is not allowed."
        }
    result = a / b
    return {
        "operation": "division",
        "operands": [a, b],
        "result": result
    }