from fastapi import APIRouter, HTTPException, status
from app.schemas.topics import *
from app.dependencies import DBSession
from app.crud.topic import *
from typing import Sequence

topic_router = APIRouter(prefix="", tags=["topics"])

@topic_router.get("/",  response_model = TopicListResponse)
async def get_all_topics(db: AsyncSession = DBSession):
    database_topics: Sequence[Topic] = await get_all_topics(db)
    return {"items": database_topics, "total": len(database_topics)}
 
@topic_router.get("/category/{category_id}",  response_model = TopicListResponse)
async def get_topics_by_category(category_id: int, db: AsyncSession = DBSession):
    database_topics: Sequence[Topic] = await get_topics_by_category(db, category_id)
    return {"items": database_topics, "total": len(database_topics)}

@topic_router.get("/{topic_id}", response_model = TopicResponse)
async def get_topic(topic_id: int, 
                        db: AsyncSession = DBSession):
    database_topic: Optional[Topic] = await get_topic_by_id(db, topic_id)
    if not database_topic: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Topic {topic_id} not found"
        )
    return database_topic
