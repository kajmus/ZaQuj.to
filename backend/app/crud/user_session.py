from typing import Sequence, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime, timezone
from sqlalchemy import update, func
from app.models.user_session import UserSession  


async def create_user_session(db: AsyncSession, id_user: int) -> UserSession:
    db_session = UserSession(id_user=id_user)
    db.add(db_session)
    await db.commit()
    await db.refresh(db_session)
    return db_session


async def get_user_session(db: AsyncSession, session_id: int) -> Optional[UserSession]:
    return await db.get(UserSession, session_id)


async def get_session_by_user(db: AsyncSession, id_user: int) -> Sequence[UserSession]:
    result = await db.execute(
        select(UserSession).where(UserSession.id_user == id_user)
    )
    return result.scalars().first()


async def delete_user_session(db: AsyncSession, session_id: int) -> bool:
    db_session = await db.get(UserSession, session_id)
    if not db_session:
        return False
    await db.delete(db_session)
    await db.commit()
    return True

async def update_session_date(db: AsyncSession, session_id: int) -> bool:
    stmt = (
        update(UserSession)
        .where(UserSession.id_session == session_id)
        
        .values(started_at=func.now())
    )
    result = await db.execute(stmt)
    await db.commit()
    
    return result.rowcount > 0