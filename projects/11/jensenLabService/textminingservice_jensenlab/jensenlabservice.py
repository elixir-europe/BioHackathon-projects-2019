import json
import logging
import urllib
from typing import List

import requests

from textminingservice.TextMiningService import TextMiningService
from textminingservice.exceptions import TextMiningServiceOperationNotSupported
from textminingservice.models.cooccurrence import CoOccurrence
from textminingservice.models.publication import Publication

logger = logging.getLogger(__name__)


class JensenLabService(TextMiningService):
    LIMIT_PER_ENTITY = 50000
    BASE_URL = "https://api.jensenlab.org"
    MENTION_URL = BASE_URL + "/Mentions?type={}&id={}&limit={}&format=json"
    COOCCURRENCES_URL = BASE_URL + "/Textmining?type1={}&id1={}&limit={}&format=json"
    COOCCURRENCES_URL_WITH_FILTER = BASE_URL + "/Textmining?type1={}&id1={}&limit={}&format=json&type2={}"
    IDS_MAPPING = {
        "CID": -1,
        "BTO": -25,
        "DOID": -26,
        "GO": -23
    }

    def __init__(self):
        super().__init__("JensenLabService", "Text-Mining api available at api.jensenlab.org")

    def get_mentions(self, entities: List, limit: int = 20) -> List[Publication]:
        entities_and_types = self.guess_types_for_entities(entities)
        publications_ids = []
        if len(entities) == 1:
            limit_per_entity = limit
        else:
            limit_per_entity = JensenLabService.LIMIT_PER_ENTITY
        for (entity, entity_type) in entities_and_types:
            publications_ids.append(self.get_mentions_for_entity(
                entity, entity_type, limit=limit_per_entity))
        publications_ids_intersection = set.intersection(*publications_ids)
        return [Publication(pm_id=pid) for pid in publications_ids_intersection][0:limit]

    def get_co_occurrences(self, entity: str, limit: int = 20, types: List[str] = None) -> List[CoOccurrence]:
        entity_type = JensenLabService.guess_type_for_entity(entity)
        if not types:
            url_cooccurrences = JensenLabService.COOCCURRENCES_URL.format(entity_type, entity, limit)
        else:
            if len(types) > 1:
                raise TextMiningServiceOperationNotSupported(
                    "Only a single type is supported as a filter by the {} service".format(self.name))
            filter_type = types[0]
            url_cooccurrences = JensenLabService.COOCCURRENCES_URL_WITH_FILTER.format(entity_type, entity, limit,
                                                                                      filter_type)
        print(url_cooccurrences)
        results = requests.get(url_cooccurrences)
        results.raise_for_status()
        cooccurrences_list = json.loads(results.content.decode().strip())
        cooccurrences_entities = cooccurrences_list[0]
        cooccurrences_results = []
        for entity2, entity2_dict in cooccurrences_entities.items():
            type2 = self.get_type2_from_url(entity2_dict)
            cooccurrences_results.append(CoOccurrence(entity2, entity2_dict['evidence'], type2))
        return cooccurrences_results

    def get_type2_from_url(self, entity2_dict):
        url = entity2_dict['url']
        query = urllib.parse.urlparse(url).query
        query_dict = urllib.parse.parse_qs(query)
        type2 = query_dict['type2'][0]
        return type2

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

    @staticmethod
    def get_mentions_for_entity(entity, entity_type, limit):
        url_mentions = JensenLabService.MENTION_URL.format(
            entity_type, entity, limit)
        results = requests.get(url_mentions)
        try:
            results.raise_for_status()
        except requests.exceptions.HTTPError:
            return set()
        publications_string = results.content.decode().strip()
        publications_list, has_more = json.loads(publications_string)
        return set(publications_list)


if __name__ == '__main__':
    text_mining_service = JensenLabService()
    print("Using service {}".format(text_mining_service.name))
    # publications = text_mining_service.get_mentions(
    #     ["DOID:10652", "DOID:10935"], limit=1000000)
    # print(", ".join([p.pm_id for p in publications]))
    cooccurrences = text_mining_service.get_co_occurrences("DOID:10652", types=['-25'], limit=10)
    print(cooccurrences)
