from src.api.base_client import BaseClient


class UsersClient(BaseClient):
    def get_all_users(self):
        return self._make_request("GET", "/users")

    def get_user_by_id(self, user_id: int):
        return self._make_request("GET", f"/users/{user_id}")

    def create_user(self, user_data: dict):
        return self._make_request("POST", "/users/add", json=user_data)

    def update_user(self, user_id: int, user_data: dict):
        return self._make_request("PATCH", f"/users/{user_id}", json=user_data)

    def rewrite_user(self, user_id: int, user_data: dict):
        return self._make_request("PUT", f"/users/{user_id}", json=user_data)

    def delete_user(self, user_id: int):
        return self._make_request("DELETE", f"/users/{user_id}")

    def search_users(self, search: str):
        return self._make_request("GET", f"/users/search?q={search}")

    def filter_users(self, filter_params: dict):
        query_string = ".".join(
            [f"key={key}&value={value}" for key, value in filter_params.items()]
        )
        return self._make_request("GET", f"/users/filter?{query_string}")

    def limit_and_skip_users(self, limit: int, skip: int, *args):
        query_string = ",".join(args)
        return self._make_request(
            "GET", f"/users?limit={limit}&skip={skip}&select={query_string}"
        )

    def sort_and_order_users(self, sort_by: str, order: str):
        return self._make_request("GET", f"/users?sortBy={sort_by}&order={order}")

    def get_user_todos(self, user_id: int):
        return self._make_request("GET", f"/users/{user_id}/todos")

    def get_user_carts(self, user_id: int):
        return self._make_request("GET", f"/users/{user_id}/carts")

    def get_user_posts(self, user_id: int):
        return self._make_request("GET", f"/users/{user_id}/posts")

    def login_user_get_tokens(self, username: str, password: str):
        payload = {"username": username, "password": password}
        return self._make_request("POST", "/user/login", json=payload)

    def get_current_auth_user(self, token: str):
        headers = {"Authorization": f"Bearer {token}"}
        return self._make_request("GET", "/user/me", headers=headers)
