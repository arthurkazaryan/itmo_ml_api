from sqlalchemy import Column, Integer, BigInteger, Float, String, DateTime, ForeignKey, Enum, UniqueConstraint, Boolean

from model.base_model import BaseModelTime


class Models(BaseModelTime):
    __tablename__ = "models"
    name = Column(String(32), nullable=False)
    price = Column(Integer, nullable=False)


class Inference(BaseModelTime):
    __tablename__ = "inference"
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    task_uuid = Column(String(36), nullable=False)
    status = Column(String(10), nullable=False)
    result = Column(Integer, nullable=True, default=None)
