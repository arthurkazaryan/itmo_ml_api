from typing import List, Optional

from pydantic import BaseModel

from schema.base_schema import FindBase, ModelBaseInfo, SearchOptions
from util.schema import AllOptional


class BaseUser(BaseModel):
    email: str = None
    # user_token: str = None
    name: str = None
    is_active: bool = None
    is_superuser: bool = None

    class Config:
        from_attributes = True


class BaseUserWithPassword(BaseUser, metaclass=AllOptional):
    password: str


class User(ModelBaseInfo, BaseUser, metaclass=AllOptional):
    ...


class FindUser(FindBase, BaseUser):
    email__eq: str
    ...


class UpsertUser(BaseUser, metaclass=AllOptional):
    ...


class FindUserResult(BaseModel):
    founds: Optional[List[User]]
    search_options: Optional[SearchOptions]
