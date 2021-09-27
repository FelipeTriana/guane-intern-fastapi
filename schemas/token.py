from pydantic import BaseModel


class TokenModel(BaseModel):
    user: str 
    email: str 
    
    
class TokenRespose(BaseModel):
    token: str 
    code: int = 200
    message: str 

   