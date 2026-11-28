from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.flashcards import FlashcardListResponse, FlashcardResponse
from app.services.flashcard_service import *
from app.dependencies import DBSession, user_session_validate
from app.crud import abcd_question as db
from app.models.abcd_question import ABCDQuestion
from app.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, Sequence

flashcard_router = APIRouter(prefix="", tags=["flashcards"])

#Switch to using get_flashcards_by_topic later
@flashcard_router.get("/",  response_model = FlashcardListResponse)
async def get_all_flashcards(session: AsyncSession = DBSession):
    questions: Sequence[ABCDQuestion] = await db.get_all_questions(session)
    flashcards: FlashcardListResponse = map_abcd_questions_seq_to_flashcard(questions)
    # in empty list is send instead of 404 if there are no flashcards assigned to the topic
    return flashcards
 
@flashcard_router.get("/topic/{topic_id}",  response_model = FlashcardListResponse)
async def get_flashcards_by_topic(topic_id: int, session: AsyncSession = DBSession):
    questions: Sequence[ABCDQuestion] = await db.get_questions_by_topic(session, topic_id)
    flashcards: FlashcardListResponse = map_abcd_questions_seq_to_flashcard(questions)
    # in empty list is send instead of 404 if there are no flashcards assigned to the topic
    return flashcards

@flashcard_router.get("/incorrect", response_model=FlashcardListResponse)
async def get_flashcards_with_incorrect_results(
    session: AsyncSession = DBSession,
    current_user: User = Depends(user_session_validate),
):
    questions = await db.get_questions_with_incorrect_answers(
        session, current_user.id_user
    )
    return map_abcd_questions_seq_to_flashcard(questions)

@flashcard_router.get(
    "/incorrect/category/{category_id}",
    response_model=FlashcardListResponse,
)
async def get_incorrect_flashcards_by_category(
    category_id: int,
    session: AsyncSession = DBSession,
    current_user: User = Depends(user_session_validate),
):
    questions = await db.get_questions_with_incorrect_answers(
        session, current_user.id_user, category_id=category_id
    )
    return map_abcd_questions_seq_to_flashcard(questions)

@flashcard_router.get(
    "/incorrect/topic/{topic_id}",
    response_model=FlashcardListResponse,
)
async def get_incorrect_flashcards_by_topic(
    topic_id: int,
    session: AsyncSession = DBSession,
    current_user: User = Depends(user_session_validate),
):
    questions = await db.get_questions_with_incorrect_answers(
        session, current_user.id_user, topic_id=topic_id
    )
    return map_abcd_questions_seq_to_flashcard(questions)

@flashcard_router.get("/{flashcard_id}", response_model = FlashcardResponse)
async def get_flashcard(flashcard_id: int, 
                        session: AsyncSession = DBSession):
    question: Optional[ABCDQuestion] = await db.get_question_by_id(session, flashcard_id) #flashcard_id the same as question_id
    flashcard: FlashcardResponse = map_abcd_question_to_flashcard(question)
    if not flashcard: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Flashcard {flashcard_id} not found"
        )
    return flashcard



"""
@flashcard_router.patch("/{flashcard_id}", response_model = FlashcardResponse)
async def update_flashcard(flashcard_id: int, flashcard_in: FlashcardUpdate):
    if flashcard_id not in fake_flashcards_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Flashcard not found"
        )

    stored_card = fake_flashcards_db[flashcard_id]

    update_data = flashcard_in.model_dump(exclude_unset=True)

    stored_card.update(update_data)

    return stored_card  

@flashcard_router.post("/", response_model=FlashcardResponse, status_code=status.HTTP_201_CREATED)
async def create_flashcard(flashcard_in: FlashcardCreate):
    new_id = max(fake_flashcards_db.keys(), default=0) + 1
    new_card = {
        "id": new_id,
        "front_text": flashcard_in.front_text,
        "back_text": flashcard_in.back_text,
    }
    fake_flashcards_db[new_id] = new_card

    #If wasnt succesfully added to the database
    if False: 
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="something"
            )

    return new_card

@flashcard_router.delete("/{flashcard_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_flashcard(flashcard_id: int):
    if flashcard_id not in fake_flashcards_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Flashcard not found"
        )

    del fake_flashcards_db[flashcard_id]
    return None # no return json with HTTP_204_NO_CONTENT
"""