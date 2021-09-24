from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from starlette.types import Message
from api import deps
 
from crud import crud_dog as crud
from models import models
from schemas.dog import Dog, DogCreate, DogUpdate, DeleteDog
from config.db import SessionLocal, engine
 
models.Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.get("/dogs/", response_model=List[Dog])
def read_dogs(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db )):
    dogs = crud.get_dogs(db, skip=skip, limit=limit)
    return dogs

@router.get("/dogs/{dog_id}", response_model=Dog)
def read_dog(dog_id: int, db: Session = Depends(deps.get_db )):
    db_dog = crud.get_dog(db, dog_id=dog_id)
    if db_dog is None:
        raise HTTPException(status_code=404, detail="Dog not found")
    return db_dog

@router.get("/dogs/is_adopted/", response_model=List[Dog])
def read_adopted_dogs(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db )):
    dogs = crud.get_adopted_dogs(db, skip=skip, limit=limit)
    return dogs    

@router.post("/dogs/{user_id}/", response_model=Dog)
def create_dog_for_user(user_id: int, dog: DogCreate, db: Session = Depends(deps.get_db )):
    return crud.create_user_dog(db=db, dog=dog, user_id=user_id)

@router.put("/dogs/{dog_id}/", response_model=Dog)  #Hay que agregar excepciones
def update_dog(dog_id: int, dog_update: DogUpdate, db: Session = Depends(deps.get_db )):
    return crud.update_dog(db=db, dog_update=dog_update, dog_id=dog_id)

@router.delete("/dogs/{dog_id}", response_model=DeleteDog)
def delete_dog_id(dog_id: int, db: Session = Depends(deps.get_db )):
    db_dog = crud.delete_dog(db, dog_id=dog_id)
    if db_dog is False:
        raise HTTPException(status_code=404, detail="Dog not found")
    return DeleteDog(msm="Eliminado exitosamente")