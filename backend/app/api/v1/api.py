#Agregator routerów do version 1

from fastapi import APIRouter, Depends, HTTPException
from fastapi import FastAPI

#can be swapped with v2, v3 versions without affecting the others
from app.api.v1.endpoints.questions import question_router
from app.api.v1.endpoints.users import user_router
from app.api.v1.endpoints.flashcards import flashcard_router
from app.api.v1.endpoints.auth import auth_router

from app.api.v1.endpoints.topics import topic_router
from app.api.v1.endpoints.categories import category_router

# All json data requests should be under /ap1 prefix to separate them from page requests
# It is declard in main.py, please dont change it
api_router = APIRouter(
    prefix="",
    tags=["api"],
    dependencies=[],
    responses={404: {"description": "Not SD"}},
)

api_router.include_router(user_router, prefix="/users", tags=["users"])
api_router.include_router(question_router, prefix="/questions", tags=["questions"])
api_router.include_router(auth_router   , prefix="/auth", tags=["auth"])
api_router.include_router(flashcard_router, prefix="/flashcards", tags=["flashcards"])
api_router.include_router(topic_router, prefix="/topics", tags=["topics"])
api_router.include_router(category_router, prefix="/categories", tags=["categories"])

@api_router.get("/")
def get_items():
    return {"message": "Hello in API service"}



