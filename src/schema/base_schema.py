from datetime import datetime
from typing import List, Optional, Union

from pydantic import BaseModel


class ModelBaseInfo(BaseModel):
    id: int = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class FindBase(BaseModel):
    ordering: Optional[str] = None
    page: Optional[int] = None
    page_size: Optional[Union[int, str]] = None


class SearchOptions(FindBase):
    total_count: Optional[int]


class FindResult(BaseModel):
    founds: Optional[List]
    search_options: Optional[SearchOptions]


class FindDateRange(BaseModel):
    created_at__lt: str
    created_at__lte: str
    created_at__gt: str
    created_at__gte: str


class Blank(BaseModel):
    pass
