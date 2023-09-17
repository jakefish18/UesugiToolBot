from src.models import (
    LearningCard,
    LearningCollection,
    LearningSession,
    LearningSessionCard,
    User,
    UserLearningCollection,
)

from .crud_learning_card import CRUDLearningCard
from .crud_learning_collection import CRUDLearningCollection
from .crud_learning_session import CRUDLearningSession
from .crud_learning_session_card import CRUDLearningSessionCard
from .crud_user import CRUDUser
from .crud_user_learning_collection import CRUDUserLearningCollection

crud_learning_card = CRUDLearningCard(LearningCard)
crud_learning_collection = CRUDLearningCollection(LearningCollection)
crud_learning_session = CRUDLearningSession(LearningSession)
crud_learning_session_card = CRUDLearningSessionCard(LearningSessionCard)
crud_user = CRUDUser(User)
crud_user_learning_collection = CRUDUserLearningCollection(UserLearningCollection)
