from sqlalchemy import Column, Integer, BigInteger, Float, String, DateTime, ForeignKey, Enum, UniqueConstraint, Boolean

from model.base_model import BaseModelTime


class User(BaseModelTime):
    __tablename__ = "user"
    email = Column(String(32), nullable=True)
    name = Column(String(32), nullable=True)
    password = Column(String(32), nullable=True)
    balance = Column(Integer, nullable=False, default=500)
    is_active = Column(Boolean, nullable=False, default=True)
    is_superuser = Column(Boolean, nullable=False, default=False)
