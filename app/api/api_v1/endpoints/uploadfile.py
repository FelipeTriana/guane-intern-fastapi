from fastapi import APIRouter, File, UploadFile

from app.crud import crud_file 

router = APIRouter()


@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return crud_file.upload_file(file) 



