import requests
import shutil
import os

from app.core.settings import API_GUANE_URL 

 
def upload_file(file: any):
    url = API_GUANE_URL
    file.filename = 'file'
    with open(f'{file.filename}',"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    files = {file.filename:  open(file.filename,'rb')}
    r = requests.post(url, files=files)
    os.remove(file.filename)
    return {"Guane content": r.content, 
            "Guane status code": r.status_code,
           }
    