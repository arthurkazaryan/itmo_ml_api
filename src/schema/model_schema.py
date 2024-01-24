from enum import Enum
from uuid import UUID

from pydantic import BaseModel
from pydantic.types import PositiveInt, PositiveFloat


class DrugType(Enum):
    d_penicillamine = "D-penicillamine"
    placebo = "Placebo"


class SexType(Enum):
    m = "M"
    f = "F"


class AscitesType(Enum):
    y = "Y"
    n = "N"


class HepatomegalyType(Enum):
    y = "Y"
    n = "N"


class SpidersType(Enum):
    y = "Y"
    n = "N"


class EdemaType(Enum):
    y = "Y"
    n = "N"


class ModelPredict(BaseModel):
    n_days: PositiveInt
    drug: DrugType
    age: PositiveInt
    sex: SexType
    ascites: AscitesType
    hepatomegaly: HepatomegalyType
    spiders: SpidersType
    edema: EdemaType
    bilirubin: PositiveFloat
    cholesterol: PositiveFloat
    albumin: PositiveFloat
    copper: PositiveFloat
    alk_phos: PositiveFloat
    sgot: PositiveFloat
    tryglicerides: PositiveFloat
    platelets: PositiveFloat
    prothrombin: PositiveFloat
    stage: PositiveFloat

    class Config:
        from_attributes = True


class ModelStatus(BaseModel):
    task_id: UUID


class ModelResponse(BaseModel):
    task_id: UUID
    status: str
    result: int = None
