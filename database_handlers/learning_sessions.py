"""
Learning sessions.

When user runs some learning collection, session starts.
Session id will be added to user row in users table.
Session ends when user wants to end or user has completed every card.
When user passes some card, card 'passed' flag becomes true in user session.
"""

from typing import List, Tuple

from database_handlers.table import TableHandler
from database_handlers import sql_queries


class LearningSessions(TableHandler):
    """
    Learning sessions table handler.
    """

    def __init__(self) -> None:
        super().__init__()
        self.open_connection()

        # Creating table if it not exists.
        self._execute(sql_queries.CREATE_LEARNING_SESSIONS_TABLE, ())

    def add_learning_session(self, learning_session_id: int, learning_collection: List[int]) -> None:
        """
        Create a learning session.

        Arguments:
            learning_session_id int - id of user learning session
            learning_collection: List[int] - list that has card ids.

        Returns:
            nothing
        """
        # Preparing data to insert.
        learning_session_cards = [(learning_session_id, card_id) for card_id in learning_collection]
        self._execute_big_insert(sql_queries.ADD_LEARNING_SESSION_CARDS, learning_session_cards)

    def get_random_cards(self, learning_session_id: int, amount: int) -> Tuple[int, List[int]]:
        """
        Get random cards from learning session. The one card 'passed' flag will be set to true.

        Arguments:
            amount - amount of cards to get
            learning_session_id - session from where cards must be taken

        Returns:
            Tuple with question card id and list of random card ids
        """
        unanswered_card_id = self._execute(
            sql_queries.GET_RANDOM_UNANSWERED_CARD, (learning_session_id, ), fetchall=True
        )[0][0]
        unclear_random_card_ids = self._execute(
            sql_queries.GET_RANDOM_CARDS, (learning_session_id, unanswered_card_id, amount - 1), fetchall=True
        )
        # Card ids in tuples with only one element.
        random_card_ids = [card_id[0] for card_id in unclear_random_card_ids]
        return unanswered_card_id, random_card_ids