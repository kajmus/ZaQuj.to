from typing import Sequence, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.topic import Topic

async def get_topic_by_id(
    db: AsyncSession, topic_id: int) -> Optional[Topic]:
    return await db.get(Topic, topic_id)


async def get_all_topics(db: AsyncSession) -> Sequence[Topic]:
    result = await db.execute(select(Topic))
    return result.scalars().all()


async def get_topics_by_category(db: AsyncSession, category_id: int) -> Sequence[Topic]:
    result = await db.execute(select(Topic).where(Topic.id_category == category_id))
    return result.scalars().all()


async def create_topic(db: AsyncSession, name: str, category_id: int) -> Topic:
    topic = Topic(name=name, id_category=category_id)
    db.add(topic)
    await db.commit()
    await db.refresh(topic)
    return topic