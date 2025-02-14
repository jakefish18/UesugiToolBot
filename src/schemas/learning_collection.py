from pydantic import BaseModel, Field


class LearningCollectionPreview(BaseModel):
    id: int 
    name: str
    owner_id: int = Field(..., serialization_alias="ownerId")
    number_of_cards: int = Field(..., serialization_alias="numberOfCards")
    number_of_downloads: int = Field(..., serialization_alias="numberOfDownloads")
