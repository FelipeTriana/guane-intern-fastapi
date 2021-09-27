from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from schemas.dog import Dog, DogCreate, DogUpdate, DeleteDog, Task
from models import model_dog
from crud import crud_user 
from crud import crud_dog 
from api import deps
from config.db import engine
from celery_worker import create_task
from core.security import verify_token
  
model_dog.Base.metadata.create_all(bind=engine)

PROTECTED = [Depends(verify_token)]

router = APIRouter()

 
@router.get("/dogs/", response_model=List[Dog])
def read_dogs(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db )):
    dogs = crud_dog.get_dogs(db, skip=skip, limit=limit)
    return dogs


@router.get("/dogs/is_adopted/", response_model=List[Dog])
def read_adopted_dogs(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db )):
    dogs = crud_dog.get_adopted_dogs(db, skip=skip, limit=limit)
    return dogs 


@router.get('/dogs/{name}', response_model=Dog)
def read_dog_by_name(dog_name: str, db: Session = Depends(deps.get_db )):
    db_dog = crud_dog.get_dog_by_name(db, dog_name=dog_name)
    if db_dog is None:
        raise HTTPException(status_code=404, detail="Dog not found")
    return db_dog


@router.post("/dogs/{user_id}/", response_model=Dog, dependencies=PROTECTED)
def create_dog_for_user(user_id: int, dog: DogCreate, db: Session = Depends(deps.get_db )):
    db_dog = crud_dog.get_dog_by_name(db, dog_name=dog.name)
    db_user = crud_user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if db_dog:
        raise HTTPException(status_code=400, detail="Name already registered")
    return crud_dog.create_user_dog(db=db, dog=dog, user_id=user_id)    


@router.put("/dogs/{dog_name}/", response_model=Dog)  
def update_dog_with_name(dog_name: str, dog_update: DogUpdate, db: Session = Depends(deps.get_db )):
    db_dog = crud_dog.get_dog_by_name(db, dog_name=dog_name)
    if db_dog is None:
        raise HTTPException(status_code=404, detail="Dog not found")
    return crud_dog.update_dog_by_name(db=db, dog_update=dog_update, dog_name=dog_name)


@router.delete("/dogs/{dog_name}", response_model=DeleteDog)
def delete_dog_by_name(dog_name: str, db: Session = Depends(deps.get_db )):
    db_dog = crud_dog.delete_dog_by_name(db, dog_name=dog_name)
    if db_dog is False:
        raise HTTPException(status_code=404, detail="Dog not found")
    return DeleteDog(msm="Successfully removed")


@router.get("/dogs/by_id/{dog_id}", response_model=Dog)
def read_dog_by_id(dog_id: int, db: Session = Depends(deps.get_db )):
    db_dog = crud_dog.get_dog(db, dog_id=dog_id)
    if db_dog is None:
        raise HTTPException(status_code=404, detail="Dog not found")
    return db_dog
 

@router.put("/dogs/by_id/{dog_id}/", response_model=Dog)  
def update_dog_with_id(dog_id: int, dog_update: DogUpdate, db: Session = Depends(deps.get_db )):
    db_dog = crud_dog.get_dog(db, dog_id=dog_id)
    if db_dog is None:
        raise HTTPException(status_code=404, detail="Dog not found")
    return crud_dog.update_dog(db=db, dog_update=dog_update, dog_id=dog_id)


@router.delete("/dogs/by_id/{dog_id}", response_model=DeleteDog)
def delete_dog_by_id(dog_id: int, db: Session = Depends(deps.get_db )):
    db_dog = crud_dog.delete_dog(db, dog_id=dog_id)
    if db_dog is False:
        raise HTTPException(status_code=404, detail="Dog not found")
    return DeleteDog(msm="Successfully removed")


@router.post("/dogs/celery/{user_id}/", response_model=Task, dependencies=PROTECTED)
async def create_dog_for_user_celery(user_id: int, dog: DogCreate, db: Session = Depends(deps.get_db )):
    db_dog = crud_dog.get_dog_by_name(db, dog_name=dog.name)
    db_user = crud_user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if db_dog:
        raise HTTPException(status_code=400, detail="Name already registered")
    crud_dog.create_user_dog(db=db, dog=dog, user_id=user_id)
    task_id = create_task.delay()
    return {'task_id': str(task_id), 'status': 'Processing'}





