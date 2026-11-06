from fastapi import APIRouter

user_router = APIRouter(prefix="", tags=["users"])

@user_router.get("/{user_id}")
async def get_user(user_id: int):
    return {"message": f"pobierz id:{user_id}"}

@user_router.get("/stats/{user_id}")
async def get_stats(user_id: int):
    return {"message": f"pokaż statystyki {user_id}"}
@user_router.post("/login")
async def login():
    return {"message": "logowanie"}
@user_router.post("/register")
async def register_user():
    return {"message": "rejestracje"}