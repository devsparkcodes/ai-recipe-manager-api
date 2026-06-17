# AI Recipe Manager API

## Project Overview

AI Recipe Manager API is a FastAPI-based backend application that allows users to manage recipes and generate AI-powered recipe suggestions using available ingredients.

This project was developed following a Spec-Driven Development approach where all features were implemented according to the provided project specification.

---

## Features

### Recipe Management (CRUD)

* Create a new recipe
* View all recipes
* View recipe by ID
* Update an existing recipe
* Delete a recipe

### AI Recipe Suggestion

* Generate recipe suggestions using available ingredients
* Powered by Groq AI

---

## Technologies Used

* FastAPI
* SQLModel
* SQLite
* Pydantic
* Groq API
* Python

---

## Project Structure

recipe-manager-api/

routes/
services/
models.py
schemas.py
database.py
config.py
main.py

---

## API Endpoints

### Create Recipe

POST /recipes

### Get All Recipes

GET /recipes

### Get Recipe By ID

GET /recipes/{id}

### Update Recipe

PUT /recipes/{id}

### Delete Recipe

DELETE /recipes/{id}

### AI Recipe Suggestion

POST /recipes/suggest

---

## Installation

1. Clone the repository

git clone <repository-url>

2. Create Virtual Environment

python -m venv venv

3. Activate Virtual Environment

Windows:

venv\Scripts\activate

4. Install Dependencies

pip install -r requirements.txt

5. Create .env File

GROQ_API_KEY=your_api_key

6. Run the Application

uvicorn main:app --reload

---

## API Documentation

Swagger UI:

http://127.0.0.1:8000/docs

---

## Learning Outcomes

* FastAPI Development
* SQLModel ORM
* CRUD Operations
* Dependency Injection
* Schema Validation
* AI Integration
* Spec-Driven Development

---

## Author

Muhammad Umar