from fastapi import APIRouter, HTTPException, status
from app.schemas.categories import CategoryListResponse, CategoryResponse
from app.dependencies import DBSession
from app.crud import category as db
from app.models.category import Category
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, Sequence

category_router = APIRouter(prefix="", tags=["categories"])

@category_router.get("/",  response_model = CategoryListResponse)
async def get_all_categories(session: AsyncSession = DBSession):
    database_categories: Sequence[Category] = await db.get_all_categories(session)
    return {"items": database_categories, "total": len(database_categories)}
 

@category_router.get("/{category_id}", response_model = CategoryResponse)
async def get_category(category_id: int, 
                        session: AsyncSession = DBSession):
    database_category: Optional[Category] = await db.get_category_by_id(session, category_id)
    if not database_category: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Category not found"
        )
    return database_category
