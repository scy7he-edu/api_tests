import pydantic


class RecipeResponseSchema(pydantic.BaseModel):
    id: int
    name: str
    ingredients: list[str] | None = None
    instructions: list[str] | None = None
    prepTimeMinutes: int | None = None
    cookTimeMinutes: int | None = None
    servings: int | None = None
    difficulty: str | None = None
    cuisine: str | None = None
    caloriesPerServing: int | None = None
    tags: list[str] | None = None
    userId: int | None = None
    image: pydantic.HttpUrl | None = None
    rating: float | None = None
    reviewCount: int | None = None
    mealType: list[str] | None = None


class RecipeListResponseSchema(pydantic.BaseModel):
    recipes: list[RecipeResponseSchema]


class AddRecipeRequestSchema(pydantic.BaseModel):
    name: str
