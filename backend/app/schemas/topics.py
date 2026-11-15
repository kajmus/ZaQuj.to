from typing import Optional
from pydantic import BaseModel, Field

class TopicBase(BaseModel):
    name : str

class TopicResponse(TopicBase):
    id: int = Field(validation_alias="id_temat")

    class Config:
        from_attributes = True

class TopicListResponse(BaseModel):
    items: list[TopicResponse]
    total: int

