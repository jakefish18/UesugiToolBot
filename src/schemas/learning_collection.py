from pydantic import BaseModel, Field

from models import LearningCollection


class LearningCollectionPreview(BaseModel):
    id: int 
    name: str
    owner_id: int = Field(..., serialization_alias="ownerId")
    number_of_cards: int = Field(..., serialization_alias="numberOfCards")
    number_of_downloads: int = Field(..., serialization_alias="numberOfDownloads")

    @classmethod
    def convert_from_learning_collection(cls, learning_collection: LearningCollection):
        return cls(
            id=learning_collection.id,
            name=learning_collection.name,
            owner_id=learning_collection.owner.id,
            number_of_cards=len(learning_collection.cards),
            number_of_downloads=len(learning_collection.users)
        )