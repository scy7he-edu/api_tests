import pydantic


class UserHairResponseSchema(pydantic.BaseModel):
    color: str
    type: str


class UserAuthSchema(pydantic.BaseModel):
    username: str
    password: str


class UserCoordinatesResponseSchema(pydantic.BaseModel):
    lat: float
    lng: float


class UserAddressResponseSchema(pydantic.BaseModel):
    address: str
    city: str
    state: str
    stateCode: str
    postalCode: str
    coordinates: UserCoordinatesResponseSchema
    country: str


class UserBankResponseSchema(pydantic.BaseModel):
    cardExpire: str
    cardNumber: str
    cardType: str
    currency: str
    iban: str


class UserCompanyResponseSchema(pydantic.BaseModel):
    department: str
    name: str
    title: str
    address: UserAddressResponseSchema


class UserCryptoResponseSchema(pydantic.BaseModel):
    coin: str
    wallet: str
    network: str


class UserResponseSchema(pydantic.BaseModel):
    id: int
    firstName: str | None = None
    lastName: str | None = None
    maidenName: str | None = None
    age: int | None = None
    gender: str | None = None
    email: str | None = None
    phone: str | None = None
    username: str | None = None
    password: str | None = None
    birthDate: str | None = None
    image: str | None = None
    bloodGroup: str | None = None
    height: float | None = None
    weight: float | None = None
    eyeColor: str | None = None
    hair: UserHairResponseSchema | None = None
    ip: str | None = None
    address: UserAddressResponseSchema | None = None
    macAddress: str | None = None
    university: str | None = None
    bank: UserBankResponseSchema | None = None
    company: UserCompanyResponseSchema | None = None
    ein: str | None = None
    ssn: str | None = None
    userAgent: str | None = None
    crypto: UserCryptoResponseSchema | None = None
    role: str | None = None


class UserListResponseSchema(pydantic.BaseModel):
    users: list[UserResponseSchema]


class UserTokensSchema(pydantic.BaseModel):
    accessToken: str
    refreshToken: str


class UserTodoSchema(pydantic.BaseModel):
    id: int
    todo: str
    completed: bool
    userId: int


class UserTodoListSchema(pydantic.BaseModel):
    todos: list[UserTodoSchema]


class AddUserRequestSchema(pydantic.BaseModel):
    firstName: str
    lastName: str
    age: int
