import pydantic


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


class CommentListSchema(pydantic.BaseModel):
    comments: list[CommentSchema]


class CreateCommentRequestSchema(pydantic.BaseModel):
    postId: int
    userId: int
    body: str
