from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String 
from sqlalchemy.orm import relationship

from config.db import Base

if TYPE_CHECKING:
    from .model_user import User


class Dog(Base):
    __tablename__ = "dogs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)
    picture = Column(String(255), index=True)
    is_adopted = Column(Boolean, default=False)
    create_date = Column(String(255), index=True)             
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="dogs")
