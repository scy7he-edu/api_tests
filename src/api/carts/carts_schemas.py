import pydantic
from src.api.base.base_schemas import BasePaginationSchema


class CartProductResponseSchema(pydantic.BaseModel):
    id: int
    title: str
    price: float
    quantity: int
    total: float
    discountPercentage: float
    discountedTotal: float | None = None
    thumbnail: pydantic.HttpUrl


class CartSchema(pydantic.BaseModel):
    id: int
    products: list[CartProductResponseSchema]
    total: float
    discountedTotal: float
    userId: int
    totalProducts: int
    totalQuantity: int


class CartListSchema(BasePaginationSchema):
    carts: list[CartSchema]


class CartProductRequestSchema(pydantic.BaseModel):
    id: int
    quantity: int


class CreateCartRequestSchema(pydantic.BaseModel):
    userId: int
    products: list[CartProductRequestSchema]
