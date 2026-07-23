import pytest

from src.utils.data_generator import product_data, invalid_ids
from src.utils.assertions import Asserts
from src.api.products.products_schemas import (
    ProductListSchema,
    ProductResponseSchema,
    ProductCategoriesListSchema,
)


@pytest.mark.products
class TestProducts:
    @pytest.mark.positive
    def test_get_all_products(self, api):
        response = api.products.get_all_products()
        response_data = Asserts.base_assertion(response, 200)
        ProductListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_signle_product(self, api):
        response = api.products.get_single_product(1)
        response_data = Asserts.base_assertion(response, 200)
        ProductResponseSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_search_products(self, api):
        response = api.products.search_products("phone")
        response_data = Asserts.base_assertion(response, 200)
        ProductListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_limit_and_skip_products(self, api):
        selection = ["id", "title", "description", "category", "price"]
        response = api.products.limit_and_skip_products(10, 10, *selection)
        response_data = Asserts.base_assertion(response, 200)
        ProductListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_sort_products(self, api):
        response = api.products.sort_products("title", "asc")
        response_data = Asserts.base_assertion(response, 200)
        ProductListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_products_categories(self, api):
        response = api.products.get_products_categories()
        assert response.status_code == 200
        response_data = response.json()
        ProductCategoriesListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_products_category_list(self, api):
        response = api.products.get_products_category_list()
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    @pytest.mark.positive
    def test_get_products_by_category(self, api):
        response = api.products.get_products_by_category("smartphones")
        response_data = Asserts.base_assertion(response, 200)
        ProductListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_add_product(self, api):
        response = api.products.add_product(product_data())
        response_data = Asserts.base_assertion(response, 201)
        ProductResponseSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_update_product(self, api):
        response = api.products.update_product(product_data(), 1)
        Asserts.base_assertion(response, 200)

    @pytest.mark.positive
    def test_rewrite_product(self, api):
        response = api.products.rewrite_product(product_data(), 1)
        Asserts.base_assertion(response, 200)

    @pytest.mark.positive
    def test_delete_product(self, api):
        response = api.products.delete_product(1)
        assert response.status_code == 200
        assert response.json().get("isDeleted") is True


class TestProductsNegative:
    @pytest.mark.negative
    @pytest.mark.parametrize("negative_product_id", invalid_ids(5, 9999, 99999))
    def test_get_invalid_product(self, api, negative_product_id):
        response = api.products.get_single_product(negative_product_id)
        assert response.status_code == 404
