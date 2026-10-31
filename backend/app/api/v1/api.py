#Agregator routerów do version 1

from fastapi import APIRouter, Depends, HTTPException
from fastapi import FastAPI

from app.api.v1.endpoints.questions import question_router
from app.api.v1.endpoints.users import user_router
from app.api.v1.endpoints.flashcards import flashcard_router

# All json data requests should be under /ap1/(version_nubmer) prefix to separate them from page requests
api_router = APIRouter(
    prefix="/api/v1",
    tags=["api"],
    dependencies=[],
    responses={404: {"description": "Not SD"}},
)

api_router.include_router(user_router, prefix="/users", tags=["users"])
api_router.include_router(question_router, prefix="/questions", tags=["questions"])
api_router.include_router(flashcard_router, prefix="/flashcards", tags=["flashcards"])

