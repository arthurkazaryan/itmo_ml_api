from sqlalchemy import Column, Integer, BigInteger, Float, String, DateTime, ForeignKey, Enum, UniqueConstraint, Boolean

from model.base_model import BaseModel, BaseModelTime


class User(BaseModelTime):
    __tablename__ = "user"
    email = Column(String(32), nullable=True)
    name = Column(String(32), nullable=True)
    password = Column(String(32), nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)
    is_superuser = Column(Boolean, nullable=False, default=False)


class UserBalance(BaseModel):
    __tablename__ = "user_balance"
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False, primary_key=True)
    balance = Column(Integer, nullable=False, default=500)
