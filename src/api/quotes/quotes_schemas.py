import pydantic
from src.api.base.base_schemas import BasePaginationSchema


class QuoteResponseSchema(pydantic.BaseModel):
    id: int
    quote: str
    author: str


class QuoteListResponseSchema(BasePaginationSchema):
    quotes: list[QuoteResponseSchema]
