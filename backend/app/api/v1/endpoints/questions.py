from fastapi import APIRouter, HTTPException, status
from app.schemas.questions import *
from app.dependencies import DBSession
from app.crud.abcd_question import *
from typing import Sequence

question_router = APIRouter(prefix="", tags=["questions"])

@question_router.get("/",  response_model = QuestionListResponse)
async def get_all_questions(db: AsyncSession = DBSession):
    database_questions: Sequence[ABCDQuestion] = await get_all_questions(db)
    return {"items": database_questions, "total": len(database_questions)}
 
@question_router.get("/topic/{topic_id}",  response_model = QuestionListResponse)
async def get_questions_by_topic(topic_id: int, db: AsyncSession = DBSession):
    database_questions: Sequence[ABCDQuestion] = await get_questions_by_topic(db, topic_id)
    return {"items": database_questions, "total": len(database_questions)}

@question_router.get("/{question_id}", response_model = QuestionResponse)
async def get_question(question_id: int, 
                        db: AsyncSession = DBSession):
    database_question: Optional[ABCDQuestion] = await get_question_by_id(db, question_id)
    if not database_question: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Question {question_id} not found"
        )
    return database_question
