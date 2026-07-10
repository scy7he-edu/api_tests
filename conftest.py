import pytest

from config import Credentials
from src.api.users_client import UsersClient


@pytest.fixture
def users_client():
    users_client = UsersClient()
    return users_client


@pytest.fixture(scope="function")
def auth_token(users_client):
    response = users_client.login_user_get_tokens(
        Credentials.username, Credentials.password
    )
    response_data = response.json()
    return response_data["accessToken"]
