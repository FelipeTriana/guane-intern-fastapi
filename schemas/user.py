from typing import List, Optional

from pydantic import BaseModel
from schemas.dog import Dog


class UserBase(BaseModel):
    name: str
    last_name: str
    email: str
    

class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]


class User(UserBase):
    id: Optional[int]
    dogs: List[Dog] = []

    class Config:
        orm_mode = True


class DeleteUser(BaseModel):
    msm: str