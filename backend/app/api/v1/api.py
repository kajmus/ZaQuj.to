#Agregator routerów do version 1

from fastapi import APIRouter, Depends, HTTPException
from fastapi import FastAPI

from app.api.v1.endpoints.questions import question_router
from app.api.v1.endpoints.users import user_router
from app.api.v1.endpoints.auth import auth_router


api_router = APIRouter(
    prefix="",
    tags=["api"],
    dependencies=[],
    responses={404: {"description": "Not SD"}},
)


api_router.include_router(user_router, prefix="/users", tags=["users"])
api_router.include_router(question_router, prefix="/questions", tags=["questions"])
api_router.include_router(auth_router   , prefix="/auth", tags=["auth"])

@api_router.get("/")
def get_items():
    return {"message": "Hello in API service"}
