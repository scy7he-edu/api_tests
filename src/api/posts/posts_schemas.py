import pydantic


class PostReactionsSchema(pydantic.BaseModel):
    likes: int
    dislikes: int


class PostSchema(pydantic.BaseModel):
    id: int
    title: str
    body: str
    tags: list[str]
    reactions: PostReactionsSchema
    views: int
    userId: int


class PostListSchema(pydantic.BaseModel):
    posts: list[PostSchema]


class PostUserCommentSchema(pydantic.BaseModel):
    id: int
    username: str
    fullName: str


class PostTagSchema(pydantic.BaseModel):
    slug: str
    name: str
    url: pydantic.HttpUrl


class PostCommentSchema(pydantic.BaseModel):
    id: int
    body: str
    postId: int
    likes: int
    user: PostUserCommentSchema


class PostListCommentsSchema(pydantic.BaseModel):
    comments: list[PostCommentSchema]


class PostTagListSchema(pydantic.RootModel[list[PostTagSchema]]):
    pass


class CreatePostRequestSchema(pydantic.BaseModel):
    userId: int
    title: str
    body: str
