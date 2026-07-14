import pydantic


class ProductSchema(pydantic.BaseModel):
    id: int
    title: str
    description: str
    category: str
    price: float


class ProductListSchema(pydantic.BaseModel):
    products: list[ProductSchema]


class CategoriesSchema(pydantic.BaseModel):
    slug: str
    name: str
    url: pydantic.HttpUrl


class CategoriesListSchema(pydantic.RootModel[list[CategoriesSchema]]):
    pass
