from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from api import deps
from crud import crud_user 
from models import model_user
from schemas.user import User, UserUpdate, UserCreate, DeleteUser
from config.db import engine

model_user.Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.get("/users/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db )):
    users = crud_user.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(deps.get_db )):
    db_user = crud_user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(deps.get_db )):
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud_user.create_user(db=db, user=user)


@router.put("/users/{user_id}/", response_model=User)   
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(deps.get_db )):
    db_user = crud_user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud_user.update_user(db=db, user_update=user_update, user_id=user_id)


@router.delete("/users/{user_id}", response_model=DeleteUser)
def delete_user_id(user_id: int, db: Session = Depends(deps.get_db )):
    db_user = crud_user.delete_user(db, user_id=user_id)
    if db_user is False:
        raise HTTPException(status_code=404, detail="User not found")
    return DeleteUser(msm="Successfully removed")
