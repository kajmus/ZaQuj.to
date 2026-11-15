from fastapi import APIRouter, HTTPException, status
from app.schemas.categories import *
from app.dependencies import DBSession
from app.crud.category import *
from typing import Sequence

category_router = APIRouter(prefix="", tags=["categories"])

@category_router.get("/",  response_model = CategoryListResponse)
async def get_all_categories(db: AsyncSession = DBSession):
    database_categories: Sequence[Category] = await get_all_categories(db)
    return {"items": database_categories, "total": len(database_categories)}
 

@category_router.get("/{category_id}", response_model = CategoryResponse)
async def get_category(category_id: int, 
                        db: AsyncSession = DBSession):
    database_category: Optional[Category] = await get_category_by_id(db, category_id)
    if not database_category: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Category not found"
        )
    return database_category
