import httpx

from src.api.carts.carts_client import CartsClient
from src.api.comments.comments_client import CommentsClient
from src.api.posts.posts_client import PostsClient
from src.api.products.products_client import ProductsClient
from src.api.quotes.quotes_client import QuotesClient
from src.api.recipes.recipes_client import RecipesClient
from src.api.users.users_client import UsersClient


class ApiManager:
    def __init__(self, base_url: str):
        self.http = httpx.Client(base_url=base_url)

        self.carts = CartsClient(self.http)
        self.comments = CommentsClient(self.http)
        self.posts = PostsClient(self.http)
        self.products = ProductsClient(self.http)
        self.quotes = QuotesClient(self.http)
        self.recipes = RecipesClient(self.http)
        self.users = UsersClient(self.http)
