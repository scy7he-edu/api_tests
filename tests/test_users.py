import pytest

from src.api.users.user_schemas import (
    UserListResponseSchema,
    UserResponseSchema,
    UserTodoListSchema,
    UserTokensSchema,
    AddUserRequestSchema,
)
from src.api.carts.carts_schemas import CartListSchema
from src.api.posts.posts_schemas import PostListSchema
from src.utils.assertions import Asserts
from src.utils.data_generator import user_data, user_auth_data, invalid_ids


@pytest.mark.users
class TestUsers:
    @pytest.mark.positive
    def test_get_users(self, api):
        response = api.users.get_all_users()
        response_data = Asserts.base_assertion(response, 200)
        assert "users" in response_data
        UserListResponseSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_single_user(self, api):
        response = api.users.get_user_by_id(2)
        response_data = Asserts.base_assertion(response, 200)
        UserResponseSchema.model_validate(response_data)
        assert response_data["id"] == 2

    @pytest.mark.negative
    @pytest.mark.parametrize("negative_id", [99999, 2435235, 12325])
    def test_get_single_negative(self, api, negative_id):
        response = api.users.get_user_by_id(negative_id)
        assert response.status_code == 404

    @pytest.mark.positive
    def test_create_user(self, api):
        response = api.users.create_user(user_data())
        response_data = Asserts.base_assertion(response, 201)
        AddUserRequestSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_update_user(self, api):
        response = api.users.update_user(1, user_data())
        response_data = Asserts.base_assertion(response, 200)
        UserResponseSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_rewrite_user(self, api):
        response = api.users.rewrite_user(1, user_data())
        response_data = Asserts.base_assertion(response, 200)
        UserResponseSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_delete_user(self, api):
        response = api.users.delete_user(1)
        response_data = response.json()
        assert response_data["isDeleted"]

    @pytest.mark.positive
    def test_search_users(self, api):
        response = api.users.search_users("John")
        response_data = Asserts.base_assertion(response, 200)
        UserListResponseSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_filter_users(self, api):
        response = api.users.filter_users({"hair.color": "Brown", "hair.type": "Curly"})
        response_data = Asserts.base_assertion(response, 200)
        UserListResponseSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_limit_skip_users(self, api):
        response = api.users.limit_and_skip_users(5, 10, "firstName", "lastName", "age")
        response_data = Asserts.base_assertion(response, 200)
        UserListResponseSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_sort_and_order_users(self, api):
        response = api.users.sort_and_order_users("id", "desc")
        response_data = Asserts.base_assertion(response, 200)
        assert response_data["users"][0]["id"] == 208

    @pytest.mark.positive
    def test_get_user_todos(self, api):
        response = api.users.get_user_todos(2)
        response_data = Asserts.base_assertion(response, 200)
        UserTodoListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_user_carts(self, api):
        response = api.users.get_user_carts(2)
        response_data = Asserts.base_assertion(response, 200)
        CartListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_user_posts(self, api):
        response = api.users.get_user_posts(3)
        response_data = Asserts.base_assertion(response, 200)
        PostListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_login_user_get_tokens(self, api):
        response = api.users.login_user_get_tokens(user_auth_data())
        response_data = Asserts.base_assertion(response, 200)
        UserTokensSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_current_auth_user(self, api, auth_token):
        response = api.users.get_current_auth_user(auth_token)
        response_data = Asserts.base_assertion(response, 200)
        assert "email" in response_data


class TestUsersNegative:
    @pytest.mark.negative
    @pytest.mark.xfail(
        reason="DummyJSON mock returns 201 literally for every kind of data :)",
        strict=True,
    )
    def test_create_invalid_user(self, api, invalid_user_payload):
        response = api.users.create_user(invalid_user_payload)
        assert response.status_code == 400

    @pytest.mark.negative
    @pytest.mark.parametrize("invalid_user_id", invalid_ids())
    def test_get_invalid_user_by_id(self, api, invalid_user_id):
        response = api.users.get_user_by_id(invalid_user_id)
        assert response.status_code == 404
