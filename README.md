# AI Recipe Manager API

A FastAPI-based backend application for managing recipes and generating AI-powered recipe suggestions from available ingredients.

## Project Overview

The AI Recipe Manager API was developed using a Spec-Driven Development approach.

The API provides endpoints for recipe management and AI-powered recipe suggestions using the Groq API.

## Features

### Recipe Management

- Create a new recipe
- Retrieve all recipes
- Retrieve a recipe by ID
- Update an existing recipe
- Delete a recipe

### AI Recipe Suggestions

Generate recipe recommendations based on available ingredients.

For example, ingredients such as:

```text
Rice, Chicken, Yogurt
```

can be used to generate a recipe suggestion with ingredients and cooking instructions.

## How It Works

The application provides two main areas of functionality:

1. **Recipe Management** — Handles CRUD operations for recipes through FastAPI endpoints.
2. **AI Recipe Suggestions** — Sends available ingredients to the Groq API and returns an AI-generated recipe suggestion.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | Backend framework |
| SQLModel | Database ORM and data modeling |
| SQLite | Database |
| Pydantic | Data validation |
| Groq API | AI-powered recipe generation |
| Git & GitHub | Version control and repository management |

## Project Structure

```text
recipe-manager-api/
│
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
```

## API Documentation

### Recipe Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/recipes` | Create a new recipe |
| GET | `/recipes` | Retrieve all recipes |
| GET | `/recipes/{id}` | Retrieve a recipe by ID |
| PUT | `/recipes/{id}` | Update a recipe |
| DELETE | `/recipes/{id}` | Delete a recipe |

### AI Suggestion

| Method | Endpoint | Description |
|---|---|---|
| POST | `/recipes/suggest` | Generate an AI-powered recipe suggestion |

## Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd recipe-manager-api
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file and add your Groq API key:

```env
GROQ_API_KEY=your_api_key
```

### 6. Run the Development Server

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI provides interactive API documentation at:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Learning Outcomes

This project helped strengthen practical understanding of:

- FastAPI development
- CRUD operations
- Dependency Injection
- Schema validation
- SQLModel ORM
- SQLite database integration
- AI API integration
- Spec-Driven Development

## Future Improvements

Potential future enhancements include:

- Improved recipe recommendation logic
- Additional recipe filtering and search functionality
- More advanced ingredient-based recommendations
- User authentication and authorization
- Deployment support

## Author

**Muhammad Umar**

Building practical applications at the intersection of software engineering and AI.

- GitHub: https://github.com/devsparkcodes
- LinkedIn: https://linkedin.com/in/devsparkcodes
