import pytest

from config import Credentials
from src.api.users_client import UsersClient
from src.api.products_client import ProductsClient
from src.api.quotes_client import QuotesClient
from src.api.comments_client import CommentsClient
from src.api.posts_client import PostsClient
from src.api.recipes_client import RecipesClient


@pytest.fixture
def users_client():
    users_client = UsersClient()
    return users_client


@pytest.fixture
def products_client():
    products_client = ProductsClient()
    return products_client


@pytest.fixture
def quotes_client():
    quotes_client = QuotesClient()
    return quotes_client


@pytest.fixture
def comments_client():
    comments_client = CommentsClient()
    return comments_client


@pytest.fixture
def posts_client():
    posts_client = PostsClient()
    return posts_client


@pytest.fixture
def recipes_client():
    recipes_client = RecipesClient()
    return recipes_client


@pytest.fixture(scope="function")
def auth_token(users_client):
    response = users_client.login_user_get_tokens(
        Credentials.username, Credentials.password
    )
    response_data = response.json()
    return response_data["accessToken"]
