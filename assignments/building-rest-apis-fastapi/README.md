# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI that manages a collection of tasks using in-memory storage, request validation, and clear HTTP responses.

## 📝 Tasks

### 🛠️ Set Up the FastAPI Application

#### Description
Create a new FastAPI app and define a health check endpoint so the server can be started and tested locally.

#### Requirements
Completed program should:

- Import `FastAPI` and create an app instance.
- Add a `GET /health` endpoint that returns a JSON response with a status message.
- Run the app locally with Uvicorn and confirm the endpoint responds successfully.

### 🛠️ Create Task Models and Endpoints

#### Description
Implement endpoints to create, list, retrieve, update, and delete tasks using Pydantic models.

#### Requirements
Completed program should:

- Define request and response models for a task.
- Add a `GET /tasks` endpoint to list all tasks.
- Add a `POST /tasks` endpoint to create a new task.
- Add a `GET /tasks/{task_id}` endpoint to retrieve one task by ID.
- Add a `PUT /tasks/{task_id}` endpoint to update an existing task.
- Add a `DELETE /tasks/{task_id}` endpoint to remove a task.

### 🛠️ Handle Validation and Errors

#### Description
Improve the API to respond clearly when a task is missing or an input is invalid.

#### Requirements
Completed program should:

- Return a `404` error when a requested task does not exist.
- Validate incoming task data with meaningful field constraints.
- Use appropriate status codes such as `201 Created` for new resources.
