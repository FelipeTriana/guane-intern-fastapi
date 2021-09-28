from fastapi import APIRouter

from app.api.api_v1.endpoints import users, dogs, token, uploadfile

api_router = APIRouter()


api_router.include_router(users.router, prefix="/api", tags=["Users"])
api_router.include_router(dogs.router, prefix="/api", tags=["Dogs"])
api_router.include_router(token.router, prefix="/api", tags=["Token"] )
api_router.include_router(uploadfile.router, prefix="/api", tags=["Uploadfile"] )
