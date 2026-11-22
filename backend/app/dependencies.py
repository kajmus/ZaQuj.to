from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import user as user_crud
from app.crud import user_session as user_session_crud
from app.core.database import get_db
from app.models.user import User

SessionHeader = APIKeyHeader(name="Session-Id", auto_error=False)
DBSession = Depends(get_db)

"""
Nie wiem do końca gdzie ta logika do sesji powinna być więc jak ktoś ma lepszy pomysł to może przenieść
~ Piotr
"""
async def refresh_user_session(db: AsyncSession, session_id: int) -> None:
    refreshed = await user_session_crud.update_session_date(db, session_id)
    if not refreshed:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Sesja wygasła. Zaloguj się ponownie.",
        )


async def user_session_validate(
    raw_session_id: str | None = Depends(SessionHeader),
    db: AsyncSession = DBSession,
) -> User:
    if not raw_session_id or not raw_session_id.isdigit():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Brak nagłówka Session-Id.",
        )

    session_id = int(raw_session_id)
    session = await user_session_crud.get_user_session(db, session_id)

    if not session:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Sesja wygasła. Zaloguj się ponownie.",
        )

    if session.started_at + timedelta(days=3) < datetime.utcnow():
        await user_session_crud.delete_user_session(db, session_id)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Sesja wygasła. Zaloguj się ponownie.",
        )

    user = await user_crud.get_user_by_id(db, session.id_user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Użytkownik nie istnieje.",
        )

    await refresh_user_session(db, session_id)
    return user