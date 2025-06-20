from app.db.db_setup import Base
from sqlalchemy import (
    Float, Column, ForeignKey, Integer, String, DateTime, func, Boolean, Enum, JSON, Text
)
from sqlalchemy.orm import relationship 


class TimestampMixin:
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)


class User(TimestampMixin, Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    firstname = Column(String(255), index=True, nullable=False)
    lastname = Column(String(255), index=True, nullable=False)
    email = Column(String(255), unique=True, nullable=True, index=True)
    phonenumber = Column(String(15), unique=True, nullable=True)
    original_password = Column(String(255), nullable=True)
    password = Column(String(255), nullable=True)
    role = Column(String(55), nullable=True)


class Notification(TimestampMixin, Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    fk_user_id = Column(Integer, ForeignKey("users.id"), index=True, nullable=True)
    message = Column(String(255), nullable=False)
    read = Column(Boolean, default=False)

class ResetPassword(TimestampMixin, Base):
    __tablename__ = "resetPassword"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    fk_user_id = Column(Integer, ForeignKey("users.id"), index=True, nullable=False)   
    otp = Column(String(25), nullable=False)