from fastapi import APIRouter

question_router = APIRouter(prefix="", tags=["users"])

@question_router.get("/{question_id}")
async def get_question(question_id: int):
    return {"message": f"Pytanie id:{question_id}"}

