from typing import List

from database_handlers.table import TableHandler
from database_handlers import sql_queries


class UserLearningCollections(TableHandler):
    """
    User learning collections handler.
    """

    def __init__(self) -> None:
        super().__init__()
        self.open_connection()

        # Creating table if it not exists.
        self._execute(sql_queries.CREATE_USER_LEARNING_COLLECTIONS_TABLE, ())

    def add_user_learning_collection(self, user_id: int, learning_collection_name: str) -> bool:
        """
        Adding a user learning collection.

        Arguments:
            user_id int - id of user who adding learning collection
            learning_collection_name str - learning collection name

        Returns:
            Bool flag which equals to True if user haven't learning collection with the same name in database.
        """

        if not self._is_user_learning_collection(user_id, learning_collection_name):
            self._execute(
                sql_queries.ADD_USER_LEARNING_COLLECTIONS, (learning_collection_name, user_id)
            )
            return True
        else:
            return False

    def get_learning_collection_id(self, user_id: int, learning_collection_name: str) -> int:
        """
        Get learning collection id by learning collection name.

        Arguments:
            learning_collection_name str - name of learning collection which id to get

        Returns:
            Learning collection id
            0 if there isn't learning collection with the same learning collection name
        """
        selected_rows = self._execute(
            sql_queries.GET_USER_LEARNING_COLLECTION_ID, (user_id, learning_collection_name), fetchall=True
        )
        return selected_rows[0][0] # Only one possible row must be.

    def get_user_learning_collection_names(self, user_id: int) -> List[str]:
        """
        Get user learning collection names.

        Arguments:
            user_id int - the user whose learning collections needed

        Returns:
            List of learning collection names
        """
        unclear_data = self._execute(sql_queries.GET_USER_LEARNING_COLLECTION_NAMES, (user_id, ), fetchall=True)
        # Because results is list of tuples, need to clear to list of strings.
        learning_collection_names = [row[0] for row in unclear_data]
        return learning_collection_names

    def _is_user_learning_collection(self, user_id: int, learning_collection_name: str) -> bool:
        """
        Checking if user have learning collection with the same name in database.

        Arguments:
            user_id int - id of user to check
            learning_collection_name str - learning collection name

        Returns:
            Bool flag which equals to True if user haven't learning collection with the same name in database.
        """
        selected_rows = self._execute(
            sql_queries.GET_USER_LEARNING_COLLECTION_ID, (user_id, learning_collection_name), fetchall=True
        )
        return len(selected_rows) != 0 # Checking that at least one row was selected.


