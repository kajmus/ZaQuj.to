from datetime import datetime
from typing import Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.test import Test
from app.models.result import Result


async def create_test(db: AsyncSession, user_id: int, mode: str) -> Test:
    new_test = Test(id_user=user_id, mode=mode)
    db.add(new_test)
    await db.commit()
    await db.refresh(new_test)
    return new_test


async def finish_test(db: AsyncSession, test_id: int) -> Test | None:
    result = await db.execute(select(Test).where(Test.id_testu == test_id))
    test = result.scalar_one_or_none()
    if test:
        test.finished_at = datetime.utcnow()
        await db.commit()
        await db.refresh(test)
    return test


async def add_result(
    db: AsyncSession,
    test_id: int,
    question_id: int,
    selected_answer: str | None = None,
    is_correct: bool | None = None,
) -> Result:
    res = Result(
        id_testu=test_id,
        id_pytanie=question_id,
        selected_answer=selected_answer,
        boolean_answer=is_correct,
        answered_at=datetime.utcnow(),
    )
    db.add(res)
    await db.commit()
    await db.refresh(res)
    return res