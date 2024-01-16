from sqlalchemy import Column, Integer, BigInteger, Float, String, DateTime, ForeignKey, Enum, UniqueConstraint, Boolean

from model.base_model import BaseModelTime


class Models(BaseModelTime):
    __tablename__ = "models"
    name = Column(String(32), nullable=False)
    price = Column(Integer, nullable=False)
