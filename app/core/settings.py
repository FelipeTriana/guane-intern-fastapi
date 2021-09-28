import os 
from dotenv import load_dotenv
 
load_dotenv()


DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_PORT = os.getenv('DB_PORT')
DB_DATABASE = os.getenv('DB_DATABASE')
SECRET = os.getenv('SECRET')
ALGORITHM = os.getenv('ALGORITHM')
TOKEN_EXPIRE = os.getenv('TOKEN_EXPIRE')
API_DOG_URL=os.getenv('API_DOG_URL')
API_GUANE_URL=os.getenv('API_GUANE_URL')