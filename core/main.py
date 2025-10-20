from fastapi import FastAPI
from core.api import protected_router
from core.config import settings


app = FastAPI()


app.include_router(protected_router)

print(f"App name: {settings.APP_NAME}")
print(f"App version: {settings.APP_VERSION}")