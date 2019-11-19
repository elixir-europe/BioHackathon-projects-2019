import json
import logging
from typing import List

import requests

from TextMiningService import TextMiningService, Publication

logger = logging.getLogger(__name__)


class JensenLabService(TextMiningService):
    BASE_URL = "https://api.jensenlab.org"
    MENTION_URL = BASE_URL + "/Mentions?type={}&id={}&limit={}&format=json"
    IDS_MAPPING = {
        "CID": -1,
        "BTO": -25,
        "DOID": -26,
    }

    def __init__(self):
        super().__init__("JensenLabService", "Text-Mining api available at api.jensenlab.org")

    def get_mentions(self, entities: List, limit: int = 20) -> List[Publication]:
        entities_and_types = self.guess_types_for_entities(entities)
        publications_ids = []
        for (entity, entity_type) in entities_and_types:
            publications_ids.append(self.get_mentions_for_entity(entity, entity_type, limit))
        publications_ids_intersection = set.intersection(*publications_ids)
        return [Publication(pm_id=pid) for pid in publications_ids_intersection]

    def get_co_occurrences(self, entity: str, limit: int = 20) -> List[str]:
        pass

    @staticmethod
    def guess_types_for_entities(entities):
        results = []
        for entity in entities:
            entity_type = JensenLabService.guess_type_for_entity(entity)
            results.append((entity, entity_type))
        return results

    @staticmethod
    def guess_type_for_entity(entity):
        for prefix, entity_type in JensenLabService.IDS_MAPPING.items():
            if entity.startswith(prefix):
                return entity_type
        return -1

    def get_mentions_for_entity(self, entity, entity_type, limit):
        url_mentions = JensenLabService.MENTION_URL.format(entity_type, entity, limit)
        results = requests.get(url_mentions)
        assert results.ok
        publications_string = results.content.decode().strip().replace('True', 'true').replace('False', 'false')
        publications_list, has_more = json.loads(publications_string)
        return set(publications_list)


if __name__ == '__main__':
    text_mining_service = JensenLabService()
    print("Using service {}".format(text_mining_service.name))
    publications = text_mining_service.get_mentions(["DOID:10652", "DOID:10654"], limit=1000000)
    print(", ".join([p.pm_id for p in publications]))
