"""
User learning collections reply markup.
"""

from models import User
from telegram_bot.keyboard_markups import reply_kbm
from utils import LearningCollectionName, list_transformation


def generate(user: User):
    user_learning_collection_names_markup: list[str] = []

    for user_learning_collection in user.learning_collections:
        user_learning_collection_name = LearningCollectionName(user_learning_collection.learning_collection.name)
        user_learning_collection_name.author = user_learning_collection.learning_collection.owner_id
        user_learning_collection_name = str(user_learning_collection_name)
        user_learning_collection_names_markup.append(list_transformation(user_learning_collection_name))

    return reply_kbm.generate(user_learning_collection_names_markup)
