
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/hello")
def hello_world(request: Request):
    return JSONResponse({"message": "Hello world"}, status_code=200)


@app.get("/welcome")
def bienvenue(request: Request, name: str = "not defined"):
    return JSONResponse({"message": f"Welcome {name}"}, status_code=200)

class Students(BaseModel):
    References : str
    FirstName : str
    LastName : str
    Age : int

array_students : []

@app.post("/students", status_code=201)
def add_students(new_students:list[Students]):
    array_students.append(new_students)
    return array_students


@app.get("/students", status_code=200)
def get_students():
    return array_students

@app.put("/students")





