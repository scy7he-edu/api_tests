import pytest

from config import Credentials
from src.api.base_client import BaseClient
from src.schemas.products_schemas import (
    ProductListSchema,
    ProductSchema,
    CategoriesListSchema,
)

credentials = Credentials()


@pytest.mark.products
class TestProducts:
    @pytest.mark.positive
    def test_get_all_products(self, products_client):
        response = products_client.get_all_products()
        response_data = BaseClient.base_assertion(response, 200)
        ProductListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_signle_product(self, products_client):
        response = products_client.get_single_product(1)
        response_data = BaseClient.base_assertion(response, 200)
        ProductSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_search_products(self, products_client):
        response = products_client.search_products("phone")
        response_data = BaseClient.base_assertion(response, 200)
        ProductListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_limit_and_skip_products(self, products_client):
        selection = ["id", "title", "description", "category", "price"]
        response = products_client.limit_and_skip_products(10, 10, *selection)
        response_data = BaseClient.base_assertion(response, 200)
        ProductListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_sort_products(self, products_client):
        response = products_client.sort_products("title", "asc")
        response_data = BaseClient.base_assertion(response, 200)
        ProductListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_products_categories(self, products_client):
        response = products_client.get_products_categories()
        assert response.status_code == 200
        response_data = response.json()
        CategoriesListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_products_category_list(self, products_client):
        response = products_client.get_products_category_list()
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    @pytest.mark.positive
    def test_get_products_by_category(self, products_client):
        response = products_client.get_products_by_category("smartphones")
        response_data = BaseClient.base_assertion(response, 200)
        ProductListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_add_product(self, products_client):
        response = products_client.add_product(credentials.product_data)
        response_data = BaseClient.base_assertion(response, 201)
        ProductSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_update_product(self, products_client):
        response = products_client.update_product(credentials.update_product, 1)
        response_data = BaseClient.base_assertion(response, 200)
        ProductSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_rewrite_product(self, products_client):
        response = products_client.rewrite_product(credentials.update_product, 1)
        response_data = BaseClient.base_assertion(response, 200)
        ProductSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_delete_product(self, products_client):
        response = products_client.delete_product(1)
        assert response.status_code == 200
        assert response.json().get("isDeleted") is True
