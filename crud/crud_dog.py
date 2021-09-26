from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from models import model_dog
from schemas.dog import DogCreate, DogUpdate
from datetime import datetime
import requests
from celery_worker import create_task

def get_dogs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_dog.Dog).offset(skip).limit(limit).all()

def get_dog(db: Session, dog_id: int):
    return db.query(model_dog.Dog).filter(model_dog.Dog.id == dog_id).first()

def get_adopted_dogs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_dog.Dog).filter(model_dog.Dog.is_adopted == True).all()

def create_user_dog(db: Session, dog: DogCreate, user_id: int):
    url = "https://dog.ceo/api/breeds/image/random"
    result = requests.get(url)
    image = result.json()
    db_dog = model_dog.Dog(**dog.dict(), picture = image['message'], create_date = datetime.now() ,owner_id=user_id)
    db.add(db_dog)
    db.commit()
    db.refresh(db_dog)
    return db_dog

def update_dog(db: Session, dog_update: DogUpdate, dog_id: int):  #Hay que agregar excepciones
    db_obj = db.query(model_dog.Dog).filter(model_dog.Dog.id == dog_id).first()
    obj_data = jsonable_encoder(db_obj)
    update_data = dog_update.dict(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(db_obj, field, update_data[field])
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_dog(db: Session, dog_id: int):
    dog_dl = db.query(model_dog.Dog).filter(model_dog.Dog.id == dog_id).first()
    if dog_dl is None:
        return False
    db.delete(dog_dl)
    db.commit()
    return True

