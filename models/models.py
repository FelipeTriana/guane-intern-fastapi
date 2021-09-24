from sqlalchemy import Boolean, Column, ForeignKey, Integer, String #, DateTime
from sqlalchemy.orm import relationship
from config.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    last_name = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True)
    

    dogs = relationship("Dog", back_populates="owner")


class Dog(Base):
    __tablename__ = "dogs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    picture = Column(String(255), index=True)
    is_adopted = Column(Boolean, default=False)
    create_date = Column(String(255), index=True)             #Cambiamos DateTime por String debido a un error
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="dogs")

