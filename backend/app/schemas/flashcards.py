from typing import Optional
from pydantic import BaseModel
from app.models.abcd_question import ABCDQuestion

class FlashcardBase(BaseModel):
    front_text: str
    back_text: str

class FlashcardResponse(FlashcardBase):
    id: int

    class Config:
        from_attributes = True

class FlashcardListResponse(BaseModel):
    items: list[FlashcardResponse]
    total: int

"""class FlashcardCreate(FlashcardBase):
    pass

class FlashcardUpdate(BaseModel):
    front_text: Optional[str] = None
    back_text: Optional[str] = None"""