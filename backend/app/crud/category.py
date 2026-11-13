from typing import Sequence, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.category import Category


async def get_category_by_id(
    db: AsyncSession, category_id: int) -> Optional[Category]:
    return await db.get(Category, category_id)


async def get_all_categories(db: AsyncSession) -> Sequence[Category]:
    result = await db.execute(select(Category))
    return result.scalars().all()


async def create_category(db: AsyncSession, name: str) -> Category:
    category = Category(name=name)
    db.add(category)
    await db.commit()
    await db.refresh(category)
    return category


