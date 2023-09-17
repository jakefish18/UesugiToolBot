from typing import Union


# Supporting classes.
class LearningCollectionName:
    """
    Learning collection name can contain two attributes:
    1. The name of learning collection.
    2. The author of learning collection.
    This class needs to be used for user inputs and outputs in telegram bot.
    """

    def __init__(self, learning_collection_input: str) -> None:
        self._input = learning_collection_input
        self.name = self._parse_learning_collection_name()
        self.author = self._parse_learning_collection_author()

    def __str__(self) -> str:
        return f"{self.name} @{self.author}"

    def _parse_learning_collection_name(self) -> str:
        """Parsing the name of learning collection."""
        if not self._is_author():
            return self._input

        learning_collection_name = self._input.split("@")[0]
        learning_collection_name = learning_collection_name.strip()
        return learning_collection_name

    def _parse_learning_collection_author(self) -> Union[str, None]:
        """
        Parsing the author of learning colleciton.
        Method returns None if there isn't such name.
        """
        if not self._is_author():
            return None

        learning_collection_author = self._input.split("@")[1]
        learning_collection_author = learning_collection_author.strip()
        return learning_collection_author

    def _is_author(self):
        return self._input.find("@") != -1


# Supporting functions.
def list_transformation(x: str) -> list[str]:
    """Returning list with single object x."""
    return [x]
