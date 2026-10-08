from fastapi import FastAPI , APIRouter
import os

base_router = APIRouter(
    prefix="/api/v1", 
    tags=["base"]
    )

@base_router.get("/")
def welcome():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION") 
    return {
        "App Name ": app_name,
        "App Version": app_version
    }

