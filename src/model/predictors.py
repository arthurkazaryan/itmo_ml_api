from sqlmodel import Field, Text

from model.base_model import BaseModel


class Models(BaseModel, table=True):
    name: str = Field(unique=True)
    cost: int = Field()
    is_active: bool = Field(default=True)
