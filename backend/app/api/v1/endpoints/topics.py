from fastapi import APIRouter, HTTPException, status
from app.schemas.topics import TopicListResponse, TopicResponse
from app.dependencies import DBSession
from app.crud import topic as db
from app.models.topic import Topic
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, Sequence

topic_router = APIRouter(prefix="", tags=["topics"])

@topic_router.get("/",  response_model = TopicListResponse)
async def get_all_topics(session: AsyncSession = DBSession):
    database_topics: Sequence[Topic] = await db.get_all_topics(session)
    return {"items": database_topics, "total": len(database_topics)}
 
@topic_router.get("/category/{category_id}",  response_model = TopicListResponse)
async def get_topics_by_category(category_id: int, session: AsyncSession = DBSession):
    database_topics: Sequence[Topic] = await db.get_topics_by_category(session, category_id)
    return {"items": database_topics, "total": len(database_topics)}

@topic_router.get("/{topic_id}", response_model = TopicResponse)
async def get_topic(topic_id: int, 
                        session: AsyncSession = DBSession):
    database_topic: Optional[Topic] = await db.get_topic_by_id(session, topic_id)
    if not database_topic: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Topic {topic_id} not found"
        )
    return database_topic
