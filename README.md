# 🍳 AI Recipe Manager API

A modern FastAPI-based backend application that helps users manage recipes and generate AI-powered recipe suggestions using available ingredients.

---

## 🚀 Project Overview

This project was developed using a Spec-Driven Development approach.

The API allows users to:

✅ Create recipes

✅ View recipes

✅ Update recipes

✅ Delete recipes

✅ Generate AI recipe suggestions using Groq AI

---

## ✨ Features

### Recipe Management

* Create a new recipe
* Retrieve all recipes
* Retrieve recipe by ID
* Update existing recipes
* Delete recipes

### AI Recipe Suggestion

Generate recipe recommendations based on available ingredients.

Example Input:

Rice, Chicken, Yogurt

Example Output:

Chicken Biryani with ingredients and cooking instructions.

---

## 🏗 Project Architecture

recipe-manager-api/

├── routes/

├── services/

├── models.py

├── schemas.py

├── database.py

├── config.py

├── main.py

├── requirements.txt

├── .gitignore

└── README.md

---

## 🛠 Technologies Used

* Python
* FastAPI
* SQLModel
* SQLite
* Pydantic
* Groq API
* Git & GitHub

---

## 📚 API Endpoints

### Recipes

POST /recipes

GET /recipes

GET /recipes/{id}

PUT /recipes/{id}

DELETE /recipes/{id}

### AI Suggestion

POST /recipes/suggest

---

## ⚙ Installation

### Clone Repository

git clone <repository-url>

### Create Virtual Environment

python -m venv venv

### Activate Environment

Windows:

venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Create .env File

GROQ_API_KEY=your_api_key

### Run Server

uvicorn main:app --reload

---

## 📖 API Documentation

Swagger UI:

http://127.0.0.1:8000/docs

---

## 🎯 Learning Outcomes

This project helped me learn:

* FastAPI Development
* CRUD Operations
* Dependency Injection
* Schema Validation
* SQLModel ORM
* AI Integration
* Spec-Driven Development

---

## 👨‍💻 Author

Muhammad Umar
