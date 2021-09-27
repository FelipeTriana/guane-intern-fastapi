from typing import List, Optional

from pydantic import BaseModel


class DogBase(BaseModel):
    name: Optional[str]
    is_adopted: Optional[bool]


class DogCreate(DogBase):
    pass


class DogUpdate(DogBase):        
    pass


class Dog(DogBase):
    id: int
    create_date: str  
    picture: str
    owner_id: int

    class Config:
        orm_mode = True


class DeleteDog(BaseModel):
    msm: str


#Celery task representation
class Task(BaseModel):
    task_id: str
    status: str