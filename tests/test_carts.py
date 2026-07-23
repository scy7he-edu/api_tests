import pytest

from src.utils.data_generator import cart_data, invalid_ids
from src.utils.assertions import Asserts
from src.api.carts.carts_schemas import CartSchema, CartListSchema


@pytest.mark.carts
class TestCarts:
    @pytest.mark.positive
    def test_get_all_carts(self, api):
        response = api.carts.get_all_carts()
        response_data = Asserts.base_assertion(response, 200)
        CartListSchema.model_validate(response_data)
        assert len(response_data) > 0

    @pytest.mark.positive
    def test_get_single_cart(self, api):
        response = api.carts.get_single_cart(1)
        response_data = Asserts.base_assertion(response, 200)
        CartSchema.model_validate(response_data)
        assert response_data["id"] == 1

    @pytest.mark.positive
    def test_get_carts_by_user(self, api):
        response = api.carts.get_carts_by_user(1)
        response_data = Asserts.base_assertion(response, 200)
        CartListSchema.model_validate(response_data)
        assert len(response_data) > 0

    @pytest.mark.positive
    def test_add_cart(self, api):
        response = api.carts.add_cart(cart_data())
        assert response.status_code == 201
        assert response.json()["id"] is not None

    @pytest.mark.positive
    def test_update_cart(self, api):
        response = api.carts.update_cart(1, cart_data())
        response_data = Asserts.base_assertion(response, 200)
        CartSchema.model_validate(response_data)
        assert response_data["id"] == 1

    @pytest.mark.positive
    def test_delete_cart(self, api):
        response = api.carts.delete_cart(1)
        assert response.status_code == 200
        assert response.json()["isDeleted"] is True


class TestCartsNegative:
    @pytest.mark.negative
    @pytest.mark.parametrize("invalid_cart_id", invalid_ids(5, 9999, 99999))
    def test_get_invalid_single_cart(self, api, invalid_cart_id):
        response = api.carts.get_single_cart(invalid_cart_id)
        assert response.status_code == 404
