from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

class FlashcardBase(BaseModel):
    front_text: str
    back_text: str

class FlashcardResponse(FlashcardBase):
    id: int = Field(validation_alias=AliasChoices("id", "id_pytanie"))

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