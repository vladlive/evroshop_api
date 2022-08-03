from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from api import router

my_app = FastAPI()
my_app.include_router(router)
