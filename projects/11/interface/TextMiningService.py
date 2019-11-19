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
    def getMentions(self, entities: List) -> List[Publication]:
        pass

    @abstractmethod
    def getCoOccurrences(self, entity: str) -> List[str]:
        pass


    


