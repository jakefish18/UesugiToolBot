from pydantic import BaseModel


class LearningCollectionPreview(BaseModel):
    id: int
    name: str
    owner_id: int
    number_of_cards: int
    number_of_downloads: int