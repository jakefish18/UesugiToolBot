import psycopg2
import psycopg2.extras
from typing import List, Tuple

from database_handlers.config import (
    DATABASE_HOST, DATABASE_USERNAME, DATABASE_NAME, DATABASE_PASSWORD
)


class TableHandler:
    """
    Base table handler class.
    """

    def __init__(self) -> None:
        self.database_host = DATABASE_HOST
        self.database_username = DATABASE_USERNAME
        self.database_name = DATABASE_NAME
        self.database_password = DATABASE_PASSWORD

    def open_connection(self) -> None:
        """
        Connecting to the database.
        Every table handler instance creates a connection.
        """
        self.connection = psycopg2.connect(
            host=self.database_host,
            user=self.database_username,
            dbname=self.database_name,
            password=self.database_password
        )

    def _close_connection(self) -> None:
        """Closing a database connection."""
        self.connection.close()

    def _create_cursor(self) -> None:
        """Creating a cursor to proccess query."""
        self.cursor = self.connection.cursor()

    def _close_cursor(self) -> None:
        """Closing a database connection cursor."""
        self.cursor.close()

    def _fetchone(self) -> Tuple:
        """Fetching one query return after the last fetch."""
        return self.cursor.fetchone()

    def _fetchall(self) -> List[Tuple]:
        """Fetching all query returns after the last fetch."""
        return self.cursor.fetchall()

    def _execute(self, query: str, data: tuple, fetchall: bool = False) -> List[Tuple]:
        """
        Executing query with given data.

        Arguments:
            query str - query to make
            data tuple - tuple of arguments to pass to query
            fetchall - flag to fetch inserted, updated, deleted, selected rows

        Returns:
            List of updated, deleted, selected, inserted rows if fetchall flag is setted to True
            else empty list with one empty tuple will be returned.
        """
        self._create_cursor()
        self.cursor.execute(query, data)
        self.connection.commit()

        if fetchall:
            query_results = self._fetchall()
            self._close_cursor()
            return query_results

        else:
            self._close_cursor()
            return []

    def _execute_big_insert(self, query: str, data: List[Tuple], fetchall: bool = False) -> List[Tuple]:
        """
        Executing query with given data.
        Unlike the usual execute, this function can be used to pass unknown count of data.

        Arguments:
            query str - query to make
            data List[Tuple] - list of tuples to insert
            fetchall - flag to fetch inserted rows

        Returns:
            List of inserted rows if fetchall flag is setted to True
            else empty list with one empty tuple will be returned.
        """
        self._create_cursor()
        psycopg2.extras.execute_values(self.cursor, query, data)
        self.connection.commit()

        if fetchall:
            query_results = self._fetchall()
            self._close_cursor()
            return query_results

        else:
            self._close_cursor()
            return []