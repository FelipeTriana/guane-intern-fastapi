from fastapi import APIRouter
from api.api_v1.endpoints import users, dogs

api_router = APIRouter()

api_router.include_router(users.router, prefix="/api", tags=["users"])
api_router.include_router(dogs.router, prefix="/api", tags=["dogs"])