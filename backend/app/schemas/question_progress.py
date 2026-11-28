from datetime import datetime

from pydantic import BaseModel, ConfigDict


class QuestionProgressUpdate(BaseModel):
    last_is_correct: bool


class QuestionProgressResponse(BaseModel):
    id_progress: int
    id_question: int
    last_is_correct: bool
    last_answered_at: datetime

    model_config = ConfigDict(from_attributes=True)
