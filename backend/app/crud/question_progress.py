from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.abcd_question import ABCDQuestion
from app.models.question_progress import QuestionProgress


async def upsert_question_progress(
    db: AsyncSession,
    user_id: int,
    question_id: int,
    last_is_correct: bool,
) -> QuestionProgress | None:
    question = await db.get(ABCDQuestion, question_id)
    if question is None:
        return None

    await db.commit()
    answered_at = datetime.now(timezone.utc).replace(tzinfo=None)
    result = await db.execute(
        select(QuestionProgress).where(
            QuestionProgress.id_user == user_id,
            QuestionProgress.id_question == question_id,
        )
    )
    progress = result.scalar_one_or_none()
    await db.commit()

    if progress is not None:
        progress.last_is_correct = last_is_correct
        progress.last_answered_at = answered_at
    else:
        progress = QuestionProgress(
            id_user=user_id,
            id_question=question_id,
            last_is_correct=last_is_correct,
            last_answered_at=answered_at,
        )
        #Preventing possible race condition in case the function gets called 2 times in short amount of time
        try:
            async with db.begin_nested():
                db.add(progress)
                await db.flush()
        except IntegrityError:
            result = await db.execute(
                select(QuestionProgress).where(
                    QuestionProgress.id_user == user_id,
                    QuestionProgress.id_question == question_id,
                )
            )
            progress = result.scalar_one_or_none()
            if progress is None:
                raise
            progress.last_is_correct = last_is_correct
            progress.last_answered_at = answered_at

    await db.commit()
    await db.refresh(progress)
    return progress
