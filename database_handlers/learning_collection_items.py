from typing import Tuple, List, Dict

from database_handlers.table import TableHandler
from database_handlers import sql_queries


class LearningCollectionItems(TableHandler):
    """
    Learning collections items handler.
    """

    def __init__(self) -> None:
        super().__init__()
        self.open_connection()

        # Creating table if it not exists.
        self._execute(sql_queries.CREATE_LEARNING_COLLECTION_ITEMS_TABLE, ())

    def add_learning_collection_items(
            self, learning_collection_id: int, learning_collection: Dict[str, str]
    ) -> None:
        """
        Adding learning collection items.

        Arguments:
            learning_collection_id - learning collection where to add items
            learning_collection_items - dict of cards, where key is card question and value is card answer

        Returns:
            nothing
        """
        # Preparing data to insert.
        learning_collection_items_to_add = []
        for card_question, card_answer in learning_collection.items():
            learning_collection_items_to_add.append((learning_collection_id, card_question, card_answer))

        self._execute_big_insert(sql_queries.ADD_LEARNING_COLLECTION_ITEMS, learning_collection_items_to_add)

    def get_learning_collection_card_ids(self, learning_collection_id: int) -> List[int]:
        """
        Get learning collections card ids.

        Arguments:
            learning_collection_id - learning collection id from where must be cards got

        Returns:
            List of card ids
        """
        unclear_card_ids = self._execute(
            sql_queries.GET_LEARNING_COLLECTION_CARD_IDS, (learning_collection_id, ), fetchall=True
        )
        # Because results is list of tuples, need to clear to list of integers.
        cards_ids = [unclear_card_id[0] for unclear_card_id in unclear_card_ids]
        return cards_ids

    def get_card_question_and_answer(self, card_id: int) -> Tuple[str, str]:
        """
        Get card question and answer by card id.

        Arguments:
            card_id int - card which question and answer need to get

        Returns:
            Tuple with 0 - question; 1 - answer
        """
        unclear_card = self._execute(sql_queries.GET_CARD, (card_id, ), fetchall=True)
        # Because results is tuple in list, need to clear to tuple.
        card = unclear_card[0]
        card_question, card_answer = card
        return card_question, card_answer
