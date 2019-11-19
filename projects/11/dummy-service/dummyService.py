import logging
from typing import List

from interface.TextMiningService import TextMiningService, Publication
from models.coocurrence import CoOccurrence

logger = logging.getLogger(__name__)


class DummyService(TextMiningService):
    def __init__(self):
        super().__init__("DummyService", "Service that returns dummy results")

    def get_mentions(self, entities: List, limit: int = 20) -> List[Publication]:
        return [Publication(pm_id="00000" + str(i)) for i in range(20)]

    def get_co_occurrences(self, entity: str, limit: int = 20, types: List[str] = []) -> List[CoOccurrence]:
        pass


if __name__ == '__main__':
    text_mining_service = DummyService()
    print("Using service {}".format(text_mining_service.name))
    publications = text_mining_service.get_mentions(["DOID:0000"])
    print(", ".join([p.pm_id for p in publications]))
