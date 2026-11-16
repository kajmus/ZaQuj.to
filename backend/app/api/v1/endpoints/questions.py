from fastapi import APIRouter, HTTPException, status
from app.schemas.questions import QuestionListResponse, QuestionResponse
from app.dependencies import DBSession
from app.crud import abcd_question as db
from app.models.abcd_question import ABCDQuestion
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, Sequence

question_router = APIRouter(prefix="", tags=["questions"])

@question_router.get("/",  response_model = QuestionListResponse)
async def get_all_questions(session: AsyncSession = DBSession):
    database_questions: Sequence[ABCDQuestion] = await db.get_all_questions(session)
    return {"items": database_questions, "total": len(database_questions)}
 
@question_router.get("/topic/{topic_id}",  response_model = QuestionListResponse)
async def get_questions_by_topic(topic_id: int, session: AsyncSession = DBSession):
    database_questions: Sequence[ABCDQuestion] = await db.get_questions_by_topic(session, topic_id)
    return {"items": database_questions, "total": len(database_questions)}

@question_router.get("/{question_id}", response_model = QuestionResponse)
async def get_question(question_id: int, 
                        session: AsyncSession = DBSession):
    database_question: Optional[ABCDQuestion] = await db.get_question_by_id(session, question_id)
    if not database_question: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Question {question_id} not found"
        )
    return database_question
