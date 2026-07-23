import pydantic


class QuoteResponseSchema(pydantic.BaseModel):
    id: int
    quote: str
    author: str


class QuoteListResponseSchema(pydantic.BaseModel):
    quotes: list[QuoteResponseSchema]
