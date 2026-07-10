import pydantic


class UserSchema(pydantic.BaseModel):
    id: int
    firstName: str
    lastName: str
    age: int


class UserListSchema(pydantic.BaseModel):
    users: list[UserSchema]


class UserTodosSchema(pydantic.BaseModel):
    id: int
    todo: str
    completed: bool
    userId: int


class UserListTodos(pydantic.BaseModel):
    todos: list[UserTodosSchema]


class UserCartsSchema(pydantic.BaseModel):
    id: int
    products: list


class UserListCarts(pydantic.BaseModel):
    carts: list[UserCartsSchema]


class UserPostsSchema(pydantic.BaseModel):
    id: int
    title: str
    body: str
    userId: int
    tags: dict


class UserListPosts(pydantic.BaseModel):
    posts: list[UserPostsSchema]


class UserTokensSchema(pydantic.BaseModel):
    accessToken: str
    refreshToken: str
