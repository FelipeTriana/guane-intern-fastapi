from typing import List, Optional
from pydantic import BaseModel


class DogBase(BaseModel):
    name: Optional[str]
    is_adopted: Optional[bool]


class DogCreate(DogBase):
    pass

class DogUpdate(DogBase):        #DOOOOOOOOOOOOOG UPDATE
    pass

class Dog(DogBase):
    id: int
    create_date: str  
    picture: str
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    last_name: str
    email: str
    
class UserUpdate(BaseModel):
    name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]

class UserCreate(UserBase):
    pass


class User(UserBase):
    id: Optional[int]
    dogs: List[Dog] = []

    class Config:
        orm_mode = True



class Del(BaseModel):
    msm: str