from abc import ABCMeta, abstractmethod
from typing import List

from textminingservice.models.coocurrence import CoOccurrence
from textminingservice.models.publication import Publication


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
    def get_co_occurrences(self, entity: str, limit: int = 20, types: List[str] = None) -> List[CoOccurrence]:
        """
        Returns a list of entities that co-appear together at publication level

        Co-occurrences at publication level.

        To-do: decide how to handle resources that can provide co-occurrences at sentence level
        """
        pass
