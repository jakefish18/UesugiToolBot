"""
API requests with prefix /learning_collection.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi_cache.decorator import cache

from schemas import LearningCollectionPreview
from models import User, UserLearningCollection
from .. import dependencies
from crud import crud_learning_collection, crud_user_learning_collection

router = APIRouter()


@router.get("/all", description="Request to get all learning collections.")
@cache(expire=120)
async def get_all(db: Session = Depends(dependencies.get_db)) -> list[LearningCollectionPreview]:
    learning_collections = crud_learning_collection.get_all_public(db)
    results: list[LearningCollectionPreview] = [
        LearningCollectionPreview.convert_from_learning_collection(lc) for lc in learning_collections  
    ]
    return results


@router.get("/search", description="Request to search learning collections by names.")
@cache(expire=120)
async def search_learning_collections(query: str, limit: int = 1, offset: int = 0, db: Session = Depends(dependencies.get_db)) -> list[LearningCollectionPreview]:
    resulting_learning_collections = crud_learning_collection.search_learning_collectoin(db, query, limit, offset)
    results: list[LearningCollectionPreview] = [
        LearningCollectionPreview.convert_from_learning_collection(lc) for lc in resulting_learning_collections  
    ]
    return results
