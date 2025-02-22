"""
API requests with prefix /user.
There are function to deal with user: auth and etc.
"""
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from models import User, UserLearningCollection
from schemas import UserOut, LearningCollectionPreview
from crud import crud_learning_collection, crud_user_learning_collection

from .. import dependencies

router = APIRouter()


@router.get("/me", description="Request to get current user profile.")
async def get_my_profile(user: User = Depends(dependencies.get_current_user)) -> UserOut:
    return user


@router.get("/me/learning_collections", description="Get user learning collections.")
async def get_my_learning_collection(db: Session = Depends(dependencies.get_db), user: User = Depends(dependencies.get_current_user)) -> list[LearningCollectionPreview]:
    results: list[LearningCollectionPreview] = []

    for user_learning_collection in user.learning_collections:
        learning_collection = user_learning_collection.learning_collection
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


@router.post("/me/learning_collections/{learning_collection_id}", description="Add learning collection to user by id.")
async def add_user_learning_collection(learning_collection_id: int, user: User = Depends(dependencies.get_current_user), db: Session = Depends(dependencies.get_db)):
    finded_learning_collection = crud_learning_collection.get(db, learning_collection_id)

    if not finded_learning_collection:
        raise HTTPException(status.HTTP_409_CONFLICT)

    if crud_user_learning_collection.is_exists(db, user, finded_learning_collection):
        raise HTTPException(status.HTTP_409_CONFLICT)

    new_user_learning_collection = UserLearningCollection(
        user_id=user.id, learning_collection_id=finded_learning_collection.id
    )
    crud_user_learning_collection.create(db, new_user_learning_collection)

    return 201


@router.delete("/me/learning_collections/{learning_collection_id}", description="Delete learning collection from user by id.")
async def delete_user_learning_collection(learning_collection_id: int, user: User = Depends(dependencies.get_current_user), db: Session = Depends(dependencies.get_db)):
    finded_learning_collection = crud_learning_collection.get(db, learning_collection_id)
    
    if not finded_learning_collection:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    user_learning_collection = crud_user_learning_collection.get_by_user_and_learning_collection(db, user, finded_learning_collection)
    if not user_learning_collection:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    
    crud_user_learning_collection.delete(db, user_learning_collection.id)
    return 204