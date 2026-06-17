from fastapi import APIRouter, Depends
from database import Session, get_session
from services import recipe_service
from schemas import RecipeCreate, RecipeResponse, RecipeUpdate, RecipeSuggestRequest, RecipeSuggestResponse

router = APIRouter(
    prefix="/recipes",
    tags=["Recipes"]
)

@router.post("/",response_model=RecipeResponse)
def create_recipe(
    recipe: RecipeCreate,
    session: Session = Depends(get_session)
    ):

    return recipe_service.create_recipe_service(
        recipe=recipe, session=session
    )

@router.get("/", response_model=list[RecipeResponse])
def get_all_recipe(
    session: Session = Depends(get_session)
    ):

    return recipe_service.get_all_recipe_service(
        session=session
    )

@router.get("/{id}", response_model=RecipeResponse)
def get_recipe_by_id(
    id: int,
    session: Session = Depends(get_session)
    ):

    return recipe_service.get_recipe_by_id_service(
        id=id, session=session
    )

@router.put("/{id}", response_model=RecipeResponse)
def update_recipe(
    id: int,
    recipe: RecipeUpdate,
    session: Session = Depends(get_session)
    ):

    return recipe_service.update_recipe(
        id=id,
        recipe=recipe,
        session=session
    )

@router.delete("/{id}")
def delete_recipe(
    id: int,
    session: Session = Depends(get_session)
    ):
    
    return recipe_service.delete_recipe(
        id=id,
        session=session
    )

@router.post("/suggest", response_model=RecipeSuggestResponse)
def recipe_suggestion(
    ingredients: RecipeSuggestRequest
    ):
    return recipe_service.suggest_recipe_service(
        ingredients=ingredients.ingredients
    )