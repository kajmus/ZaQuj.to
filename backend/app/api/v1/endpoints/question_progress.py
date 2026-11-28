from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import question_progress as progress_crud
from app.dependencies import DBSession, user_session_validate
from app.models.user import User
from app.schemas.question_progress import QuestionProgressResponse, QuestionProgressUpdate

question_progress_router = APIRouter(prefix="", tags=["question-progress"])


@question_progress_router.put(
    "/{question_id}",
    response_model=QuestionProgressResponse,
)
async def save_question_progress(
    question_id: int,
    progress_data: QuestionProgressUpdate,
    db: AsyncSession = DBSession,
    current_user: User = Depends(user_session_validate),
):
    progress = await progress_crud.upsert_question_progress(
        db,
        current_user.id_user,
        question_id,
        progress_data.last_is_correct,
    )
    if progress is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Question {question_id} not found",
        )
    return progress
