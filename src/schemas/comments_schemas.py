import pydantic


class CommentSchema(pydantic.BaseModel):
    id: int
    body: str
    postId: int
    likes: int
    user: dict


class CommentListSchema(pydantic.BaseModel):
    comments: list[CommentSchema]
