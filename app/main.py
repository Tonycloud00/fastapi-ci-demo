
from fastapi import FastAPI
from app.todo import TodoList

app = FastAPI()
todo_list = TodoList()

@app.get("/")
def home():
    return {"message": "FastAPI is running"}

@app.post("/add/{item}")
def add_item(item: str):
    todo_list.add(item)
    return {"todos": todo_list.get_all()}

@app.get("/todos")
def get_todos():
    return {"todos": todo_list.get_all()}
