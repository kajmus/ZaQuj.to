from fastapi import APIRouter, HTTPException, status
from app.schemas.flashcards import FlashcardCreate, FlashcardResponse, FlashcardUpdate, FlashcardListResponse

flashcard_router = APIRouter(prefix="", tags=["flashcards"])

fake_flashcards_db = {
    1: {"id": 1, "front_text": "Tis but a scratch.", "back_text": "A scratch? Your arm's off"},
    2: {"id": 2, "front_text": "He's not the Messiah", "back_text": "he's a very naughty boy."},
}

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

@flashcard_router.get("/",  response_model = FlashcardListResponse)
async def get_flashcard():
    return {
        "items": list(fake_flashcards_db.values()),
        "total": len(fake_flashcards_db)
    }      #replace with database read

@flashcard_router.get("/{flashcard_id}", response_model = FlashcardResponse)
async def get_flashcard(flashcard_id: int):
    if flashcard_id not in fake_flashcards_db: #replace with database check
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Flashcard not found"
        )
    return fake_flashcards_db[flashcard_id] #replace with database read

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