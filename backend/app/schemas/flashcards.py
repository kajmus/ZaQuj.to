from typing import Optional
from pydantic import BaseModel

class FlashcardBase(BaseModel):
    front_text: str
    back_text: str

class FlashcardCreate(FlashcardBase):
    pass

class FlashcardUpdate(BaseModel):
    front_text: Optional[str] = None
    back_text: Optional[str] = None

class FlashcardResponse(FlashcardBase):
    id: int

    class Config: #makes it so the 
        from_attributes = True

class FlashcardListResponse(BaseModel):
    items: list[FlashcardResponse]
    total: int