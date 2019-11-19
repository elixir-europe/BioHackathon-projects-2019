import logging
from typing import List

from interface.TextMiningService import TextMiningService, Publication

logger = logging.getLogger(__name__)


class DummyService(TextMiningService):
    def __init__(self):
        super().__init__("DummyService", "Service that returns dummy results")

    def get_mentions(self, entities: List, limit: int = 20) -> List[Publication]:
        return [Publication(pm_id="00000" + str(i)) for i in range(20)]

    def get_co_occurrences(self, entity: str) -> List[str]:
        pass
