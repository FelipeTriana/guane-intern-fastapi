from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from models import model_user
from models import model_dog
from schemas.user import UserCreate, UserUpdate
from config.db import engine
  
def get_user(db: Session, user_id: int):
    return db.query(model_user.User).filter(model_user.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(model_user.User).filter(model_user.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_user.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    db_user = model_user.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_update: UserUpdate, user_id: int):   #Hay que agregar excepciones
    db_obj = db.query(model_user.User).filter(model_user.User.id == user_id).first()
    obj_data = jsonable_encoder(db_obj)
    update_data = user_update.dict(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(db_obj, field, update_data[field])
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
    
def delete_user(db: Session, user_id: int):
    user_dl = db.query(model_user.User).filter(model_user.User.id == user_id).first()
    if user_dl is None:
        return False
    dogs_dl = db.query(model_dog.Dog).filter(model_dog.Dog.owner_id == user_id).all()
    for i in dogs_dl:
        print(i)
        db.delete(i)
        db.commit()
    db.delete(user_dl)
    db.commit()
    return True
