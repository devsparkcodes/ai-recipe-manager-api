from pydantic import BaseModel, Field
from typing import Literal

class RecipeBase(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=100
    )

    ingredients: str = Field(
        min_length=5,
        max_length=1000
    )

    instructions: str = Field(
        min_length=10,
        max_length=5000
    )

    cuisine_type: str = Field(
        min_length=3,
        max_length=50
    )

    difficulty: Literal[
        "easy",
        "medium",
        "hard"
    ]

class RecipeCreate(RecipeBase):
    pass

class RecipeUpdate(RecipeBase):
    name: str | None = Field(
        default=None,
        min_length=3,
        max_length=100
    )

    ingredients: str | None = Field(
        default=None,
        min_length=5,
        max_length=1000
    )

    instructions: str | None = Field(
        default=None,
        min_length=10,
        max_length=5000
    )

    cuisine_type: str | None = Field(
        default=None,
        min_length=3,
        max_length=50
    )

    difficulty: Literal[
        "easy",
        "medium",
        "hard"
    ] | None = None

class RecipeResponse(RecipeBase):
    id: int

class RecipeSuggestRequest(BaseModel):
    ingredients: str = Field(
        min_length=3,
        max_length=1000
    )

class RecipeSuggestResponse(BaseModel):
    name: str
    ingredients: list[str]
    instructions: list[str]