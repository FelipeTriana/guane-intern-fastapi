from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import relationship

from config.db import Base

if TYPE_CHECKING:
    from .model_dog import Dog  


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    last_name = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True)
    
    dogs = relationship("Dog", back_populates="owner")
    