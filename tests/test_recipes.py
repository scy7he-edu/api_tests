import pytest

from src.api.recipes.recipes_schemas import (
    AddRecipeRequestSchema,
    RecipeResponseSchema,
    RecipeListResponseSchema,
)
from src.utils.assertions import Asserts
from src.utils.data_generator import recipe_data, invalid_ids


@pytest.mark.recipes
class TestRecipes:
    @pytest.mark.positive
    def test_get_all_recipes(self, api):
        response = api.recipes.get_all_recipes()
        response_data = Asserts.base_assertion(response, 200)
        RecipeListResponseSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_single_recipe(self, api):
        response = api.recipes.get_single_recipe(1)
        response_data = Asserts.base_assertion(response, 200)
        RecipeResponseSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_search_recipes(self, api):
        response = api.recipes.search_recipes("Margherita")
        response_data = Asserts.base_assertion(response, 200)
        RecipeListResponseSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_limit_skip_recipes(self, api):
        selection = [
            "id",
            "name",
            "ingredients",
            "instructions",
            "prepTimeMinutes",
            "cookTimeMinutes",
            "servings",
            "difficulty",
            "cuisine",
            "caloriesPerServing",
            "tags",
            "userId",
        ]
        response = api.recipes.limit_skip_recipes(10, 10, *selection)
        response_data = Asserts.base_assertion(response, 200)
        RecipeListResponseSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_sort_recipes(self, api):
        response = api.recipes.sort_recipes("id", "asc")
        response_data = Asserts.base_assertion(response, 200)
        RecipeListResponseSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_all_recipes_tags(self, api):
        response = api.recipes.get_all_recipes_tags()
        assert isinstance(response.json(), list)

    @pytest.mark.positive
    def test_get_recipes_by_tag(self, api):
        response = api.recipes.get_recipes_by_tag("Pakistani")
        response_data = Asserts.base_assertion(response, 200)
        RecipeListResponseSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_recipes_by_meal(self, api):
        response = api.recipes.get_recipes_by_meal("snack")
        response_data = Asserts.base_assertion(response, 200)
        RecipeListResponseSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_add_recipe(self, api):
        response = api.recipes.add_recipe(recipe_data())
        response_data = Asserts.base_assertion(response, 200)
        AddRecipeRequestSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_update_recipe(self, api):
        recipe_update = {"name": "Test recipe"}
        response = api.recipes.update_recipe(1, recipe_update)
        assert response.status_code == 200
        RecipeResponseSchema.model_validate(response.json())

    @pytest.mark.positive
    def test_delete_recipe(self, api):
        response = api.recipes.delete_recipe(1)
        assert response.status_code == 200


class TestRecipesNegative:
    @pytest.mark.negative
    @pytest.mark.parametrize("invalid_recipe_id", invalid_ids())
    def test_get_invalid_recipe(self, api, invalid_recipe_id):
        response = api.recipes.get_single_recipe(invalid_recipe_id)
        assert response.status_code == 404
