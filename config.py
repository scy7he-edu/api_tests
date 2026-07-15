from dataclasses import dataclass, field

from src.utils.data_generator import fake


@dataclass
class Credentials:
    URL: str = "https://dummyjson.com"
    firstName: str = field(default_factory=fake.first_name)
    lastName: str = field(default_factory=fake.last_name)
    age: int = field(default_factory=lambda: fake.pyint(18, 90))
    username: str = "emilys"
    password: str = "emilyspass"

    @property
    def user_data(self) -> dict:
        return {"firstName": self.firstName, "lastName": self.lastName, "age": self.age}

    @property
    def product_data(self) -> dict:
        return {
            "id": 999,
            "title": "Test Item",
            "description": "some test item, heh",
            "category": "test item, obviously",
            "price": 17.99,
        }

    @property
    def update_product(self) -> dict:
        return {
            "title": "test item",
            "description": "some test item, again.",
            "category": "yep, test item",
            "price": 99.99,
        }

    @property
    def comment_data(self) -> dict:
        return {"body": "some test comment, yo!", "postId": 3, "userId": 5}

    @property
    def post_data(self) -> dict:
        return {"title": "test post title", "userId": 5, "body": "test post body"}

    @property
    def recipe_data(self) -> dict:
        return {"id": 999, "name": "test meal name"}
