from database_handlers.table import TableHandler
from database_handlers import sql_queries


class Users(TableHandler):
    """
    Users table handler.
    There are functions to add user and to get user id or telegram id.
    """

    def __init__(self) -> None:
        super().__init__()
        self.open_connection()

        # Creating table if it not exists.
        self._execute(sql_queries.CREATE_USERS_TABLE, ())

    def add_user(self, telegram_id: str) -> bool:
        """
        User adding into table.

        Arguments:
            telegram_id str - new user telegram_id

        Returns:
            Bool flag which equals to True if user with the same telegram id isn't in database
        """
        if not self._is_user(telegram_id):
            self._execute(sql_queries.ADD_USER, (telegram_id, ))
            return True
        else:
            return False

    def get_user_id(self, telegram_id: str) -> int:
        """
        Get user id by telegram id.

        Arguments:
            telegram_id str - telegram id of the user to get user id

        Returns:
            User id
            0 if there isn't user with the same telegram id
        """
        selected_rows = self._execute(sql_queries.GET_USER_ID, (telegram_id,), fetchall=True)
        if len(selected_rows) != 0:
            return selected_rows[0][0]
        else:
            return 0

    def set_user_learning_session(self, user_id: int, learning_session_id: int) -> None:
        """
        Set user learning session to session id.

        Arguments:
            user_id - the user whose session id to change
            session_id - new session id value

        Return:
            nothing
        """
        self._execute(sql_queries.SET_USER_LEARNING_SESSION_ID, (learning_session_id, user_id))

    def _is_user(self, telegram_id: str) -> bool:
        """
        Checking if there is a user with given telegram_id.

        Arguments:
             telegram_id str - telegram_id to check.

        Returns:
            Bool flag which equals to True if there is user with the same telegram id in database
        """
        selected_rows = self._execute(sql_queries.GET_USER, (telegram_id, ), fetchall=True)
        return len(selected_rows) != 0 # Checking that at least one row was selected.
