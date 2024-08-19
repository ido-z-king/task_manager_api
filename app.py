from pydantic import BaseModel
from fastapi import FastAPI
import datetime
import uvicorn

app = FastAPI()

class Task(BaseModel):
    id : str
    title : str
    description : datetime.date
    creation_time : datetime.date
    deadline: str
    priority: int
    user: str
    
class User(BaseModel):
    id: str
    username: str
    password:str
    
@app.get("/")
def welcome():
    return {"message": "welcome to idozes task manager"}

@app.get("/tasks")
def get_all_tasks():
    """returns all the users tasks in a list of names priority and deadline
    """
    pass

app.get("/tasks/{task_name}")
def get_task_by_name(task_name):
    """get a task by the task name and return the task info

    Args:
        task_name (_type_): _description_
    """
    pass

@app.post("/")
def add_task():
    """add a user task
    """
    pass
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    
    