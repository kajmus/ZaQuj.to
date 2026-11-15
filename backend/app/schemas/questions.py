from typing import Optional
from pydantic import BaseModel, Field

class QuestionBase(BaseModel):
    text: str
    correct_answer: str
    wrong_answer_1: str
    wrong_answer_2: str
    wrong_answer_3: str

class QuestionResponse(QuestionBase):
    id: int = Field(validation_alias="id_pytanie")

    class Config:
        from_attributes = True

class QuestionListResponse(BaseModel):
    items: list[QuestionResponse]
    total: int

