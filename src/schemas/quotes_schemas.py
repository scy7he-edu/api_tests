import pydantic


class QuotesSchema(pydantic.BaseModel):
    id: int
    quote: str
    author: str


class QuotesListSchema(pydantic.BaseModel):
    quotes: list[QuotesSchema]
