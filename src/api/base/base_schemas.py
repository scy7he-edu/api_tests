from pydantic import BaseModel, ConfigDict


class BasePaginationSchema(BaseModel):
    model_config = ConfigDict(extra="forbid")

    total: int
    skip: int
    limit: int
