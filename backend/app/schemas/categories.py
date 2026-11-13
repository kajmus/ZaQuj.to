from typing import Optional
from pydantic import BaseModel, Field

class CategoryBase(BaseModel):
    name : str

class CategoryResponse(CategoryBase):
    id: int = Field(validation_alias="id_category")

    class Config:
        from_attributes = True

class CategoryListResponse(BaseModel):
    items: list[CategoryResponse]
    total: int

