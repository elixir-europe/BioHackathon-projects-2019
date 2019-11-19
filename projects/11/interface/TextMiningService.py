from abc import ABCMeta, abstractmethod
from typing import List


class Publication():
    def __init__(self, pmc_id, pm_id, doi, preprint_id, other_id):
        self.pmc_id = pmc_id
        self.pm_id = pm_id
        self.doi = doi
        self.preprint_id = preprint_id
        self.other_id = other_id


class TextMiningService(metaclass=ABCMeta):

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def getMentions(self, entities: List[str], limit: int = 20) -> List[Publication]:
        """Returs a list of publications for a given list of entity IDs in which the entities appear.

        Arguments:
            entities {List[str]} -- [description]

        Keyword Arguments:
            limit {int} -- [description] (default: {20})

        Returns:
            List[Publication] -- [description]
        """
        pass

    @abstractmethod
    def getCoOccurrences(self, entity: str) -> List[str]:
        """
        Co-occurrences at publication level.

        To-do: decide how to handle resources that can provide co-occurrences at sentence level
        """
        pass
