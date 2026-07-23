import pydantic


class ProductDimensionsResponseSchema(pydantic.BaseModel):
    width: float
    height: float
    depth: float


class ProductReviewsResponseSchema(pydantic.BaseModel):
    rating: int
    comment: str
    date: str
    reviewerName: str
    reviewerEmail: str


class ProductMetaResponseSchema(pydantic.BaseModel):
    createdAt: str
    updatedAt: str
    barcode: str
    qrCode: str


class ProductResponseSchema(pydantic.BaseModel):
    id: int
    title: str
    description: str | None = None
    category: str | None = None
    price: float | None = None
    discountPercentage: float | None = None
    rating: float | None = None
    stock: int | None = None
    tags: list[str] | None = None
    brand: str | None = None
    sku: str | None = None
    weight: int | None = None
    dimensions: ProductDimensionsResponseSchema | None = None
    warrantyInformation: str | None = None
    shippingInformation: str | None = None
    availabilityStatus: str | None = None
    reviews: list[ProductReviewsResponseSchema] | None = None
    returnPolicy: str | None = None
    minimumOrderQuantity: int | None = None
    meta: ProductMetaResponseSchema | None = None
    thumbnail: str | None = None
    images: list[str] | None = None


class ProductCategoriesSchema(pydantic.BaseModel):
    slug: str
    name: str
    url: pydantic.HttpUrl


class ProductCategoriesListSchema(pydantic.RootModel[list[ProductCategoriesSchema]]):
    pass


class ProductListSchema(pydantic.BaseModel):
    products: list[ProductResponseSchema]


class CreateProductRequestSchema(pydantic.BaseModel):
    title: str
    description: str
    category: str
    price: float
