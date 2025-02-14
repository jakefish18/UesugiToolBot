from pydantic import BaseModel, Field


class LearningCollectionPreview(BaseModel):
    id: int 
    name: str
    owner_id: int = Field(..., alias="ownerId")
    number_of_cards: int = Field(..., alias="numberOfCards")
    number_of_downloads: int = Field(..., alias="numberOfDownloads")