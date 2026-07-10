import pytest

from config import Credentials
from src.api.base_client import BaseClient
from src.schemas.user_schemas import (
    UserListCarts,
    UserListPosts,
    UserListSchema,
    UserListTodos,
    UserSchema,
    UserTokensSchema,
)

credentials = Credentials()


@pytest.mark.positive
def test_get_users(users_client):
    response = users_client.get_all_users()
    response_data = BaseClient.base_assertion(response, 200)
    assert "users" in response_data
    UserListSchema.model_validate(response_data)


@pytest.mark.positive
def test_get_single_user(users_client):
    response = users_client.get_user_by_id(2)
    response_data = BaseClient.base_assertion(response, 200)
    UserSchema.model_validate(response_data)
    assert response_data["id"] == 2


@pytest.mark.negative
@pytest.mark.parametrize("negative_id", [99999, 2435235, 12325])
def test_get_single_negative(users_client, negative_id):
    response = users_client.get_user_by_id(negative_id)
    assert response.status_code == 404


@pytest.mark.positive
def test_create_user(users_client):
    user_data = credentials.user_data
    response = users_client.create_user(user_data)
    response_data = BaseClient.base_assertion(response, 201)
    UserSchema.model_validate(response_data)


@pytest.mark.positive
def test_update_user(users_client):
    user_data: dict = {"age": credentials.age}
    response = users_client.update_user(1, user_data)
    BaseClient.base_assertion(response, 200)


@pytest.mark.positive
def test_rewrite_user(users_client):
    user_data = credentials.user_data
    response = users_client.rewrite_user(1, user_data)
    BaseClient.base_assertion(response, 200)


@pytest.mark.positive
def test_delete_user(users_client):
    response = users_client.delete_user(1)
    response_data = response.json()
    assert response_data["isDeleted"]


@pytest.mark.positive
def test_search_users(users_client):
    response = users_client.search_users("John")
    response_data = BaseClient.base_assertion(response, 200)
    UserListSchema.model_validate(response_data)


@pytest.mark.positive
def test_filter_users(users_client):
    response = users_client.filter_users({"hair.color": "Brown", "hair.type": "Curly"})
    response_data = BaseClient.base_assertion(response, 200)
    UserListSchema.model_validate(response_data)


@pytest.mark.positive
def test_limit_skip_users(users_client):
    response = users_client.limit_and_skip_users(5, 10, "firstName", "lastName", "age")
    response_data = BaseClient.base_assertion(response, 200)
    UserListSchema.model_validate(response_data)


@pytest.mark.positive
def test_sort_and_order_users(users_client):
    response = users_client.sort_and_order_users("id", "desc")
    response_data = BaseClient.base_assertion(response, 200)
    assert response_data["users"][0]["id"] == 208


@pytest.mark.positive
def test_get_user_todos(users_client):
    response = users_client.get_user_todos(2)
    response_data = BaseClient.base_assertion(response, 200)
    UserListTodos.model_validate(response_data)


@pytest.mark.positive
def test_get_user_carts(users_client):
    response = users_client.get_user_carts(2)
    response_data = BaseClient.base_assertion(response, 200)
    UserListCarts.model_validate(response_data)


@pytest.mark.positive
def test_get_user_posts(users_client):
    response = users_client.get_user_posts(3)
    response_data = BaseClient.base_assertion(response, 200)
    UserListPosts.model_validate(response_data)


@pytest.mark.positive
def test_login_user_get_tokens(users_client):
    response = users_client.login_user_get_tokens(
        Credentials.username, Credentials.password
    )
    response_data = BaseClient.base_assertion(response, 200)
    UserTokensSchema.model_validate(response_data)
    assert response_data["username"] == Credentials.username


@pytest.mark.positive
def test_get_current_auth_user(users_client, auth_token):
    response = users_client.get_current_auth_user(auth_token)
    response_data = BaseClient.base_assertion(response, 200)
    assert response_data["username"] == Credentials.username
    assert "email" in response_data
