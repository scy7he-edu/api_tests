from src.api.base_client import BaseClient


class RecipesClient(BaseClient):
    def get_all_recipes(self):
        return self._make_request("GET", "/recipes")

    def get_single_recipe(self, recipe_id: int):
        return self._make_request("GET", f"/recipes/{recipe_id}")

    def search_recipes(self, query: str):
        return self._make_request("GET", f"/recipes/search?q={query}")

    def limit_skip_recipes(self, limit: int, skip: int, *args):
        selection = ",".join(args)
        return self._make_request(
            "GET", f"/recipes?limit={limit}&skip={skip}&select={selection}"
        )

    def sort_recipes(self, sort_by: str, order: str):
        return self._make_request("GET", f"/recipes?sortBy={sort_by}&order={order}")

    def get_all_recipes_tags(self):
        return self._make_request("GET", "/recipes/tags")

    def get_recipes_by_tag(self, tag: str):
        return self._make_request("GET", f"/recipes/tag/{tag}")

    def get_recipes_by_meal(self, meal_type: str):
        return self._make_request("GET", f"/recipes/meal-type/{meal_type}")

    def add_recipe(self, recipe_data: dict):
        return self._make_request("POST", "/recipes/add", json=recipe_data)

    def update_recipe(self, recipe_id: int, recipe_data: dict):
        return self._make_request("PATCH", f"/recipes/{recipe_id}", json=recipe_data)

    def delete_recipe(self, recipe_id: int):
        return self._make_request("DELETE", f"/recipes/{recipe_id}")
