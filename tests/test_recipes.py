import pytest

from config import Credentials
from src.api.base_client import BaseClient
from src.schemas.recipes_schemas import RecipeSchema, RecipeListSchema

credentials = Credentials()


@pytest.mark.recipes
class TestRecipes:
    @pytest.mark.positive
    def test_get_all_recipes(self, recipes_client):
        response = recipes_client.get_all_recipes()
        response_data = BaseClient.base_assertion(response, 200)
        RecipeListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_single_recipe(self, recipes_client):
        response = recipes_client.get_single_recipe(1)
        response_data = BaseClient.base_assertion(response, 200)
        RecipeSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_search_recipes(self, recipes_client):
        response = recipes_client.search_recipes("Margherita")
        response_data = BaseClient.base_assertion(response, 200)
        RecipeListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_limit_skip_recipes(self, recipes_client):
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
        response = recipes_client.limit_skip_recipes(10, 10, *selection)
        response_data = BaseClient.base_assertion(response, 200)
        RecipeListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_sort_recipes(self, recipes_client):
        response = recipes_client.sort_recipes("id", "asc")
        response_data = BaseClient.base_assertion(response, 200)
        RecipeListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_all_recipes_tags(self, recipes_client):
        response = recipes_client.get_all_recipes_tags()
        assert isinstance(response.json(), list)

    @pytest.mark.positive
    def test_get_recipes_by_tag(self, recipes_client):
        response = recipes_client.get_recipes_by_tag("Pakistani")
        response_data = BaseClient.base_assertion(response, 200)
        RecipeListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_recipes_by_meal(self, recipes_client):
        response = recipes_client.get_recipes_by_meal("snack")
        response_data = BaseClient.base_assertion(response, 200)
        RecipeListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_add_recipe(self, recipes_client):
        response = recipes_client.add_recipe(credentials.recipe_data)
        BaseClient.base_assertion(response, 200)

    @pytest.mark.positive
    def test_update_recipe(self, recipes_client):
        recipe_update = {"name": "Test recipe"}
        response = recipes_client.update_recipe(1, recipe_update)
        assert response.status_code == 200
        RecipeSchema.model_validate(response.json())

    @pytest.mark.positive
    def test_delete_recipe(self, recipes_client):
        response = recipes_client.delete_recipe(1)
        assert response.status_code == 200
