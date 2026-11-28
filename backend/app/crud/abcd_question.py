
from typing import Sequence, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.abcd_question import ABCDQuestion
from app.models.question_progress import QuestionProgress
from app.models.topic import Topic

async def get_questions_by_topic(db: AsyncSession, topic_id: int) -> Sequence[ABCDQuestion]:
    result = await db.execute(
        select(ABCDQuestion).where(ABCDQuestion.id_temat == topic_id)
    )
    return result.scalars().all()

async def get_question_by_id(
    db: AsyncSession, question_id: int) -> Optional[ABCDQuestion]:
    return await db.get(ABCDQuestion, question_id)

"""Może być zbyt wolna dla dużej ilości pytań. W takim wypadku trzeba albo używać get_questions_by_topic
albo nałożyć jakiś limit"""
async def get_all_questions(db: AsyncSession) -> Sequence[ABCDQuestion]:
    result = await db.execute(select(ABCDQuestion))
    return result.scalars().all()

async def get_questions_with_incorrect_answers(
    db: AsyncSession,
    user_id: int,
    category_id: Optional[int] = None,
    topic_id: Optional[int] = None,
) -> Sequence[ABCDQuestion]:
    query = (
        select(ABCDQuestion)
        .join(QuestionProgress, QuestionProgress.id_question == ABCDQuestion.id_pytanie)
        .where(
            QuestionProgress.id_user == user_id,
            QuestionProgress.last_is_correct.is_(False),
        )
        .order_by(QuestionProgress.last_answered_at.desc())
    )

    if category_id is not None:
        query = query.join(Topic, ABCDQuestion.id_temat == Topic.id_temat).where(
            Topic.id_category == category_id
        )
    if topic_id is not None:
        query = query.where(ABCDQuestion.id_temat == topic_id)

    result = await db.execute(query)
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