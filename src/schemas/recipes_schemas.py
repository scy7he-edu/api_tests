import pydantic


class RecipeSchema(pydantic.BaseModel):
    id: int
    name: str
    ingredients: list
    instructions: list
    prepTimeMinutes: int
    cookTimeMinutes: int
    servings: int
    difficulty: str
    cuisine: str
    caloriesPerServing: int
    tags: list
    userId: int


class RecipeListSchema(pydantic.BaseModel):
    recipes: list[RecipeSchema]
