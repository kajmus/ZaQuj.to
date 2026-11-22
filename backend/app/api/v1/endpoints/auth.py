from fastapi import APIRouter, Depends, HTTPException, status
from app.core.security import our_hash
from app.schemas import UserRegister , SessionVerifySchema
from app.crud.user import * 
from app.crud.user_session import *
from app.dependencies import DBSession, user_session_validate
from app.models.user import User
from app.models.user_session import UserSession
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

auth_router = APIRouter(prefix="",tags =["auth"])

# POST    /auth/login    Loguje użytkownika i tworzy sesję
# GET    /auth/me    Zwraca dane aktualnie zalogowanego użytkownika
# POST    /auth/logout    Kończy sesję

@auth_router.get("")
def get_auth():
    return {"message": "Welcome in authorization service"}



@auth_router.post("/login")
async def post_auth_login(user_reg: UserRegister, db: AsyncSession = DBSession ):
    if not user_reg:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Wrong request")
    
    user_data_db =await get_user_by_login(db, user_reg.name)

    if not user_data_db:
        raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User login doesnt exist")
    
    hashed_request_password = our_hash(user_reg.password)

    if not hashed_request_password == user_data_db.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Password doesn't match")

    existing_session = await get_session_by_user(db, user_data_db.id_user)

    if existing_session:
        session_id= existing_session.id_session
    else:    
        new_session = await create_user_session(db, user_data_db.id_user )
        session_id  = new_session.id_session
    
        
        
    return session_id

@auth_router.post("/logout")
async def post_auth_logout(data: SessionVerifySchema,  db: AsyncSession =DBSession ):
    result = await db.execute(select(UserSession).where(UserSession.id_session == data.session_id))
    session = result.scalars().first()
    
    if session:
        await db.delete(session)
        await db.commit()

 
    return {"message": "Wylogowano pomyślnie"}

@auth_router.delete("/session/{session_id_r}")
async def auth_delete_session(session_id_r: int, db: AsyncSession = DBSession ):
    result = await delete_user_session(db, session_id =session_id_r)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sesja o podanym ID nie istnieje.")
        
    return None
        
    
@auth_router.get("/me")
async def check_session_me(user: User = Depends(user_session_validate)):
    return {
        "id_user": user.id_user,
        "login": user.login
    }
