"""
API requests with prefix /learning_collection.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi_cache.decorator import cache

from schemas import LearningCollectionPreview
from .. import dependencies
from crud import crud_learning_collection

router = APIRouter()


@router.get("/all", description="Request to get all learning collections.")
@cache(expire=120)
async def get_all(db: Session = Depends(dependencies.get_db)) -> list[LearningCollectionPreview]:
    learning_collections = crud_learning_collection.get_all(db)
    results: list[LearningCollectionPreview] = []

    for learning_collection in learning_collections:
        results.append(
            LearningCollectionPreview(
                id=learning_collection.id,
                name=learning_collection.name,
                owner_id=learning_collection.owner.id,
                number_of_cards=len(learning_collection.cards),
                number_of_downloads=len(learning_collection.users)
            )
        )

    return results