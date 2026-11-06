from typing import Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.abcd_question import ABCDQuestion


async def get_questions_by_topic(db: AsyncSession, topic_id: int) -> Sequence[ABCDQuestion]:
    result = await db.execute(
        select(ABCDQuestion).where(ABCDQuestion.id_temat == topic_id)
    )
    return result.scalars().all()


async def create_question(
    db: AsyncSession,
    text: str,
    topic_id: int,
    correct_answer: str,
    wrong_1: str,
    wrong_2: str,
    wrong_3: str,
) -> ABCDQuestion:
    question = ABCDQuestion(
        text=text,
        id_temat=topic_id,
        correct_answer=correct_answer,
        wrong_answer_1=wrong_1,
        wrong_answer_2=wrong_2,
        wrong_answer_3=wrong_3,
    )
    db.add(question)
    await db.commit()
    await db.refresh(question)
    return question