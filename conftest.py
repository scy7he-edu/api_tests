import pytest

from src.api.users_client import UsersClient


@pytest.fixture
def users_client():
    users_client = UsersClient()
    return users_client
