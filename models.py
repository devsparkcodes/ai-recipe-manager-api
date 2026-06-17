from sqlmodel import SQLModel, Field

class Recipe(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    ingredients: str
    instructions: str
    cuisine_type: str
    difficulty: str