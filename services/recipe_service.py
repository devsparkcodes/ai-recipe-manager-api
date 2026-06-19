import json

from models import Recipe
from config import GROQ_API_KEY

from fastapi import HTTPException
from sqlmodel import select
from groq import Groq


def create_recipe_service(recipe, session):
    recipe_data = Recipe(**recipe.model_dump())

    session.add(recipe_data)
    session.commit()
    session.refresh(recipe_data)

    return recipe_data

def get_all_recipe_service(session):
    statement = select(Recipe)
    get_recipe_data = session.exec(statement).all()

    if not get_recipe_data:
        raise HTTPException(
            status_code=404,
            detail="Recipes not found"
        )

    return get_recipe_data

def get_recipe_by_id_service(id, session):
    get_one_recipe_data = session.get(Recipe, id)

    if not get_one_recipe_data:
        raise HTTPException(
            status_code=404,
            detail=f"Recipe with ID {id} not found."
        )

    return get_one_recipe_data

def update_recipe(id, recipe, session):
    recipe_data = session.get(Recipe, id)

    if not recipe_data:
        raise HTTPException(
            status_code=404,
            detail=f"Recipe with ID {id} not found."
        )
    
    update_data = recipe.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(recipe_data, key, value)

    session.add(recipe_data)
    session.commit()
    session.refresh(recipe_data)

    return recipe_data

def delete_recipe(id, session):
    recipe_data = session.get(Recipe, id)

    if not recipe_data:
        raise HTTPException(
            status_code=404,
            detail=f"Recipe with ID {id} not found."
        )
    
    session.delete(recipe_data)
    session.commit()

    return {
        "message": f"Recipe with ID {id} deleted successfully.",
        "recipe": recipe_data.model_dump()
    }

client = Groq(
        api_key=GROQ_API_KEY
    )

def suggest_recipe_service(ingredients):
    prompt = f"""
    Suggest a recipe using: {ingredients}

    Return ONLY valid JSON like:
    {{
    "name": "Recipe Name",
    "ingredients": ["item1", "item2"],
    "instructions": ["step1", "step2"]
    }}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    raw = response.choices[0].message.content

    cleaned = raw.replace("```json", "").replace("```", "").strip()

    try:
        recipe_json = json.loads(cleaned)
        return recipe_json

    except json.JSONDecodeError:
        raise HTTPException(
            status_code=400,
            detail="Please provide valid ingredients."
        )