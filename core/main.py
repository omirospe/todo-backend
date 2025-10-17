from fastapi import FastAPI
from core.api import protected_router

app = FastAPI()


app.include_router(protected_router)