from fastapi import FastAPI

from api.api_v1.api import api_router

app = FastAPI(title="guane-intern-fastapi")


app.include_router(api_router)
