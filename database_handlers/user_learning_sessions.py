"""
User learning sessions.
"""

from typing import List

from database_handlers.table import TableHandler
from database_handlers import sql_queries


class UserLearningSessions(TableHandler):
    """
    User learning sessions table handler.
    """

    def __init__(self) -> None:
        super().__init__()
        self.open_connection()

        # Creating table if it not exists.
        self._execute(sql_queries.CREATE_USER_LEARNING_SESSIONS_TABLE, ())

    def create_user_learning_session(self, user_id: int, learning_collection_id: int) -> int:
        """
        Creating new user session.

        Arguments:
            user_id - user, who is starting new session
            learning_collection_id - the learning collection the user wants to start

        Return:
            New session id
        """
        learning_session_id = self._execute(
            sql_queries.CREATE_USER_LEARNING_SESSION, (user_id, learning_collection_id), fetchall=True
        )
        learning_session_id = learning_session_id[0][0]
        return learning_session_id
