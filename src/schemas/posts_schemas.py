import pydantic


class PostSchema(pydantic.BaseModel):
    id: int
    title: str
    body: str
    tags: list
    reactions: dict
    views: int
    userId: int


class PostListSchema(pydantic.BaseModel):
    posts: list[PostSchema]


class PostTagSchema(pydantic.BaseModel):
    slug: str
    name: str
    url: pydantic.HttpUrl


class PostTagListSchema(pydantic.RootModel[list[PostTagSchema]]):
    pass


class PostCommentsSchema(pydantic.BaseModel):
    id: int
    body: str
    postId: int
    likes: int
    user: dict


class PostCommentsListSchema(pydantic.BaseModel):
    comments: list[PostCommentsSchema]
