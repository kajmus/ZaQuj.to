from typing import Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.user import User


async def get_user_by_id(db: AsyncSession, user_id: int) -> User | None:
    result = await db.execute(select(User).where(User.id_user == user_id))
    return result.scalar_one_or_none()


async def get_user_by_login(db: AsyncSession, login: str) -> User | None:
    result = await db.execute(select(User).where(User.login == login))
    return result.scalar_one_or_none()


async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100) -> Sequence[User]:
    result = await db.execute(select(User).offset(skip).limit(limit))
    return result.scalars().all()

async def delete_user(db: AsyncSession, user_id: int) -> bool:
    user = await db.get(User,user_id) 
    if not user:
        return False
    await db.delete(user)
    await db.commit()
    return True
    
async def create_user(db: AsyncSession, login: str, password_hash: str) -> User:
    new_user = User(login=login, password=password_hash)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user