import logging
from typing import List

from textminingservice.TextMiningService import TextMiningService
from textminingservice.models.cooccurrence import CoOccurrence
from textminingservice.models.publication import Publication

logger = logging.getLogger(__name__)


class DummyService(TextMiningService):
    def __init__(self):
        super().__init__("DummyService", "Service that returns dummy results")

    def get_mentions(self, entities: List, limit: int = 20) -> List[Publication]:
        return [Publication(pm_id="00000" + str(i)) for i in range(limit)]

    def get_co_occurrences(self, entity: str, limit: int = 20, types: List[str] = None) -> List[CoOccurrence]:
        values = []
        for idx in range(limit):
            entity_code = f'{entity}_{idx}'
            count = int(idx * idx)
            co_occur = CoOccurrence(entity_code, count)
            values.append(co_occur)
        return values


if __name__ == '__main__':
    text_mining_service = DummyService()
    print("Using service {}".format(text_mining_service.name))
    publications = text_mining_service.get_mentions(["DOID:0000"])
    print(", ".join([p.pm_id for p in publications]))
    cooccurrences = text_mining_service.get_co_occurrences('DOID:0000')
    print(cooccurrences)
