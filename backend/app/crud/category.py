from typing import Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.category import Category
from app.models.topic import Topic


async def get_categories(db: AsyncSession) -> Sequence[Category]:
    result = await db.execute(select(Category))
    return result.scalars().all()


async def create_category(db: AsyncSession, name: str) -> Category:
    category = Category(name=name)
    db.add(category)
    await db.commit()
    await db.refresh(category)
    return category


async def get_topics_by_category(db: AsyncSession, category_id: int) -> Sequence[Topic]:
    result = await db.execute(select(Topic).where(Topic.id_category == category_id))
    return result.scalars().all()


async def create_topic(db: AsyncSession, name: str, category_id: int) -> Topic:
    topic = Topic(name=name, id_category=category_id)
    db.add(topic)
    await db.commit()
    await db.refresh(topic)
    return topic