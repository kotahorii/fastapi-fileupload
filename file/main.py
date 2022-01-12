from fastapi import FastAPI
from .routes import fileupload

app = FastAPI()

app.include_router(fileupload.router)
