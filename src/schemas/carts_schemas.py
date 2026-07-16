import pydantic


class CartSchema(pydantic.BaseModel):
    id: int
    products: list
    total: float
    discountedTotal: float
    userId: int
    totalProducts: int
    totalQuantity: int


class CartListSchema(pydantic.BaseModel):
    carts: list[CartSchema]
