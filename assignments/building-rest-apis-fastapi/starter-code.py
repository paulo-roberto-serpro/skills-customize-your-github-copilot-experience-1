from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    description: str = ""


class Task(TaskCreate):
    id: int


tasks: List[Task] = []


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/tasks", response_model=List[Task])
def list_tasks():
    return tasks


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: TaskCreate):
    new_task = Task(id=len(tasks) + 1, **task.model_dump())
    tasks.append(new_task)
    return new_task


# TODO: implement GET /tasks/{task_id}
# TODO: implement PUT /tasks/{task_id}
# TODO: implement DELETE /tasks/{task_id}
