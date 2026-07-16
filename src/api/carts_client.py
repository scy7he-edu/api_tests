from src.api.base_client import BaseClient


class CartsClient(BaseClient):
    def get_all_carts(self):
        return self._make_request("GET", "/carts")

    def get_single_cart(self, cart_id: int):
        return self._make_request("GET", f"/carts/{cart_id}")

    def get_carts_by_user(self, user_id: int):
        return self._make_request("GET", f"/carts/user/{user_id}")

    def add_cart(self, cart_data: dict):
        return self._make_request("POST", "/carts/add", json=cart_data)

    def update_cart(self, cart_id: int, cart_data: dict):
        return self._make_request("PATCH", f"/carts/{cart_id}", json=cart_data)

    def delete_cart(self, cart_id: int):
        return self._make_request("DELETE", f"/carts/{cart_id}")
