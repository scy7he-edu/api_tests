from faker import Faker

from src.api.carts.carts_schemas import (
    CreateCartRequestSchema,
    CartProductRequestSchema,
)
from src.api.comments.comments_schemas import CreateCommentRequestSchema
from src.api.posts.posts_schemas import CreatePostRequestSchema
from src.api.products.products_schemas import CreateProductRequestSchema
from src.api.recipes.recipes_schemas import AddRecipeRequestSchema
from src.api.users.user_schemas import AddUserRequestSchema, UserAuthSchema

fake = Faker()

INVALID_USER_PAYLOADS = [
    ({"firstName": 12345, "lastName": "Doe", "age": 25}, "firstName_is_numeric"),
    ({"firstName": "John", "lastName": "Doe", "age": -10}, "age_is_negative"),
    ({"firstName": "John", "lastName": "Doe", "age": "twenty"}, "age_is_string"),
    ({}, "empty_body"),
]


def invalid_ids(count: int = 5, min_id: int = 999, max_id: int = 9999) -> list[int]:
    return [fake.random_int(min_id, max_id) for _ in range(count)]


def user_data(
    first_name: str | None = None,
    last_name: str | None = None,
    age: int | None = None,
    **kwargs,
) -> AddUserRequestSchema:
    return AddUserRequestSchema(
        firstName=first_name if first_name is not None else fake.first_name(),
        lastName=last_name if last_name is not None else fake.last_name(),
        age=age if age is not None else fake.random_int(18, 90),
        **kwargs,
    )


def user_auth_data(
    username: str = "emilys", password: str = "emilyspass"
) -> UserAuthSchema:
    return UserAuthSchema(username=username, password=password)


def product_data(
    title: str = "Test item",
    description: str = "Test description",
    category: str = "Test category",
    price: float = 17.99,
) -> CreateProductRequestSchema:
    return CreateProductRequestSchema(
        title=title,
        description=description,
        category=category,
        price=price,
    )


def update_product(
    title: str = "Test product",
    description: str = "Test description",
    category: str = "Test category",
    price: float = 99.99,
) -> CreateProductRequestSchema:
    return CreateProductRequestSchema(
        title=title, description=description, category=category, price=price
    )


def comment_data(
    body: str | None = None,
    post_id: str | None = None,
    user_id: int | None = None,
    **kwargs,
) -> CreateCommentRequestSchema:
    return CreateCommentRequestSchema(
        body=body if body is not None else fake.sentence(),
        postId=post_id if post_id is not None else fake.random_int(1, 100),
        userId=user_id if user_id is not None else fake.random_int(1, 100),
        **kwargs,
    )


def post_data(
    title: str | None = None,
    body: str | None = None,
    user_id: int | None = None,
    **kwargs,
) -> CreatePostRequestSchema:
    return CreatePostRequestSchema(
        title=title if title is not None else fake.sentence(),
        body=body if body is not None else fake.text(),
        userId=user_id if user_id is not None else fake.random_int(1, 100),
        **kwargs,
    )


def recipe_data(name: str = "Test meal") -> AddRecipeRequestSchema:
    return AddRecipeRequestSchema(name=name)


def cart_data(
    user_id: int | None = None, products_data: list[dict] | None = None
) -> CreateCartRequestSchema:
    if user_id is None:
        user_id = fake.random_int(1, 100)

    if products_data is None:
        products_data = [
            {"id": fake.random_int(1, 50), "quantity": fake.random_int(1, 5)}
        ]

    products = [CartProductRequestSchema(**item) for item in products_data]
    return CreateCartRequestSchema(userId=user_id, products=products)
