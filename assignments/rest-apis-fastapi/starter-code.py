from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Task API", description="A simple REST API for managing tasks")

# In-memory storage for tasks
tasks = []

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

@app.get("/")
def read_root():
    return {"message": "Welcome to the Task API"}

# TODO: Add your CRUD endpoints here