import pydantic


class UserSchema(pydantic.BaseModel):
    id: int
    firstName: str
    lastName: str
    age: int


class UserListSchema(pydantic.BaseModel):
    users: list[UserSchema]
