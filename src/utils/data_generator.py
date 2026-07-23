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
    first_name: str = fake.name(),
    last_name: str = fake.last_name(),
    age: int = fake.random_int(18, 90),
) -> AddUserRequestSchema:
    return AddUserRequestSchema(firstName=first_name, lastName=last_name, age=age)


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
    user_id: int = 5, post_id: int = 3, body: str = "Some test comment"
) -> CreateCommentRequestSchema:
    return CreateCommentRequestSchema(userId=user_id, postId=post_id, body=body)


def post_data(
    user_id: int = 5, title: str = "Test post title", body: str = "Test post body"
) -> CreatePostRequestSchema:
    return CreatePostRequestSchema(userId=user_id, title=title, body=body)


def recipe_data(name: str = "Test meal") -> AddRecipeRequestSchema:
    return AddRecipeRequestSchema(name=name)


def cart_data(
    user_id: int = 1, products_data: list[dict] | None = None
) -> CreateCartRequestSchema:
    if products_data is None:
        products_data = [
            {
                "id": 144,
                "quantity": 4,
            },
            {"id": 98, "quantity": 1},
        ]
        products = [CartProductRequestSchema(**product) for product in products_data]

    return CreateCartRequestSchema(userId=user_id, products=products)
