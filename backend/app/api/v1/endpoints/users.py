from fastapi import APIRouter , HTTPException, status
from app.crud.user import * 
from app.dependencies import *
from sqlalchemy.exc import IntegrityError
from app.schemas import UserRegister
from app.services import our_hash

user_router = APIRouter(prefix="", tags=["users"])



@user_router.get("")
async def get_users_(db: AsyncSession = DBSession):
    result = await get_users(db,skip=0,limit=100)
    return result



@user_router.get("/id/{user_id}")
async def get_user_by_id_id(user_id: str, db: AsyncSession = DBSession):
    result = await get_user_by_id(db, user_id)
    if not result:
        raise HTTPException(status_code=409)#te errory do poprawy
    return result

@user_router.get("/login/{login_name}")
async def get_user_by_login_login(login_name: str, db: AsyncSession = DBSession):
    result = await get_user_by_login(db, login_name)
    if not result:
        raise HTTPException(status_code=409)#te errory do poprawy
    return result

@user_router.post("/register", status_code=status.HTTP_201_CREATED)
async def post_user_register(user_reg: UserRegister, db: AsyncSession = DBSession, ):
    try:
        result = await create_user(db, user_reg.name, our_hash(user_reg.password ))
        return result
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Conflict: User.name already in the data base")
        

@user_router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_delete(user_id: int, db: AsyncSession = DBSession):
    result = await delete_user(db, user_id=user_id)
    if not result:
    
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Użytkownik o podanym ID nie istnieje.")
    
    return None
    




@user_router.get("/stats/{user_id}")
async def get_stats(user_id: int):
    return {"message": f"pokaż statystyki {user_id}"}