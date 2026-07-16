import pytest

from config import Credentials
from src.api.base_client import BaseClient
from src.schemas.carts_schemas import CartSchema, CartListSchema

credentials = Credentials()


@pytest.mark.carts
class TestCarts:
    @pytest.mark.positive
    def test_get_all_carts(self, carts_client):
        response = carts_client.get_all_carts()
        response_data = BaseClient.base_assertion(response, 200)
        CartListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_single_cart(self, carts_client):
        response = carts_client.get_single_cart(1)
        response_data = BaseClient.base_assertion(response, 200)
        CartSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_carts_by_user(self, carts_client):
        response = carts_client.get_carts_by_user(1)
        response_data = BaseClient.base_assertion(response, 200)
        CartListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_add_cart(self, carts_client):
        response = carts_client.add_cart(credentials.cart_data)
        assert response.status_code == 201

    @pytest.mark.positive
    def test_update_cart(self, carts_client):
        response = carts_client.update_cart(1, credentials.cart_data)
        response_data = BaseClient.base_assertion(response, 200)
        CartSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_delete_cart(self, carts_client):
        response = carts_client.delete_cart(1)
        assert response.status_code == 200
