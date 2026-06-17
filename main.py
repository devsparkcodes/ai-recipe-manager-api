from fastapi import FastAPI
from database import create_db_and_tables
from routes.recipe_routes import router as recipe_router

create_db_and_tables()

app = FastAPI()

app.include_router(recipe_router)