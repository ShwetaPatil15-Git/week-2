# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a RESTful API using the FastAPI framework in Python. You'll create endpoints to perform basic CRUD (Create, Read, Update, Delete) operations on a simple resource like a list of tasks or items. This assignment will help you understand API design, routing, request/response handling, and data validation in a modern web framework.

## 📝 Tasks

### 🛠️ Set Up FastAPI Application

#### Description
Initialize a new FastAPI application with basic configuration and create a root endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Import FastAPI and create an app instance
- Define a GET endpoint at "/" that returns a JSON response with a welcome message
- Include proper type hints and documentation strings
- Run the server locally to test the endpoint

### 🛠️ Implement CRUD Endpoints

#### Description
Add endpoints for managing a collection of items (e.g., tasks or notes). Implement GET, POST, PUT, and DELETE operations with in-memory storage.

#### Requirements
Completed program should:

- Use a list or dictionary to store items in memory
- Create a GET endpoint at "/items" to retrieve all items
- Create a POST endpoint at "/items" to add a new item with required fields (e.g., id, title, description)
- Create a GET endpoint at "/items/{item_id}" to retrieve a specific item by ID
- Create a PUT endpoint at "/items/{item_id}" to update an existing item
- Create a DELETE endpoint at "/items/{item_id}" to remove an item
- Handle cases where items are not found (return 404 status)
- Include request/response models using Pydantic for validation