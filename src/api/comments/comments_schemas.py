import pydantic
from src.api.base.base_schemas import BasePaginationSchema


class CommentUserResponseSchema(pydantic.BaseModel):
    id: int
    username: str
    fullName: str


class CommentSchema(pydantic.BaseModel):
    id: int
    body: str
    postId: int
    likes: int
    user: CommentUserResponseSchema


class CommentListSchema(BasePaginationSchema):
    comments: list[CommentSchema]


class CreateCommentRequestSchema(pydantic.BaseModel):
    postId: int
    userId: int
    body: str
