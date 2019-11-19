from abc import ABCMeta, abstractmethod
from typing import List
from models.publication import Publication
from models.coocurrence import CoOccurrence


class TextMiningService(metaclass=ABCMeta):

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def get_mentions(self, entities: List[str], limit: int = 20) -> List[Publication]:
        """Returns a list of publications for a given list of entity IDs in which the entities appear.

        Arguments:
            entities {List[str]} -- [description]

        Keyword Arguments:
            limit {int} -- [description] (default: {20})

        Returns:
            List[Publication] -- [description]
        """
        pass

    @abstractmethod
    def get_co_occurrences(self, entity: str, limit: int = 20) -> List[CoOccurrence]:
        """
        Co-occurrences at publication level.

        To-do: decide how to handle resources that can provide co-occurrences at sentence level
        """
        pass
