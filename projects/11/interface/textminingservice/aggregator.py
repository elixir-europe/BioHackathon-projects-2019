import json
import sys
import traceback
from collections import defaultdict
from typing import List, Dict

from textminingservice_biokb.biokb import BioKBService
from textminingservice_jensenlab.jensenlabservice import JensenLabService
from textminingservice_pmc_europe.pmc_europe import PMC_Europe_Service
from textminingservice.models.cooccurrence import CoOccurrence
from textminingservice.models.publication import Publication
from textminingservice.exceptions import TextMiningServiceOperationNotSupported
from textminingservice import logger

import asyncio
from functools import partial


class Aggregator():
    def __init__(self):
        pass

    def aggregate_mentions(self, pub_collections: Dict):
        pub_dict = defaultdict(dict)
        for service, pub_lst in pub_collections.items():
            for pub in pub_lst:
                if pub.id in pub_dict:
                    publication = pub_dict[pub.id]['info']
                    pub_dict[pub.id]['info'] = Publication.merge_publications(
                        publication, pub)
                    pub_dict[pub.id]['score'] += 1
                    pub_dict[pub.id]['resources'].append(service)
                else:
                    pub_dict[pub.id]['info'] = pub
                    pub_dict[pub.id]['score'] = 1
                    pub_dict[pub.id]['resources'] = [service]

        for pub_id in pub_dict:
            pub_dict[pub_id]['info'] = pub_dict[pub_id]['info'].as_dict()

        return sorted(pub_dict.values(), key=lambda x: x['score'], reverse=True)

    def aggregate_cooccurrences(self, entity_collections: Dict):
        co_dict = defaultdict(dict)
        for service, co_lst in entity_collections.items():
            # sort desc by score
            for idx, co in enumerate(sorted(co_lst, key=lambda c: c.score, reverse=True)):
                if co.entity in co_dict:
                    co_dict[co.entity]['score'] += idx
                    co_dict[co.entity]['resources'].append(service)
                else:
                    co_dict[co.entity]['info'] = co
                    co_dict[co.entity]['score'] = idx
                    co_dict[co.entity]['resources'] = [service]

        for entity in co_dict:
            co_dict[entity]['info'].score = None
            co_dict[entity]['info'] = co_dict[entity]['info'].as_dict()

        return sorted(co_dict.values(), key=lambda x: x['score'], reverse=True)


class TextMiningDeMultiplexer:
    def __init__(self):
        biokb = BioKBService()
        jensen = JensenLabService()
        pmc = PMC_Europe_Service()
        self.services = [biokb, jensen, pmc]
        self.agg = Aggregator()

    #  ____ ____ ___    _  _ ____ _  _ ___ _ ____ _  _ ____
    #  | __ |___  |     |\/| |___ |\ |  |  | |  | |\ | [__
    #  |__] |___  |     |  | |___ | \|  |  | |__| | \| ___]
    #

    @staticmethod
    async def wrap_get_mentions(loop, service: 'TextMiningService', entities: List[str], limit: int = 20) -> List[dict]:
        results = []
        try:
            results = await loop.run_in_executor(None, partial(service.get_mentions, entities, limit=limit))
        except AssertionError:
            details = sys.exc_info()[0]
            logger.info(
                f'AssertionError from service {service}: {details}')
        except Exception:
            details = sys.exc_info()[0]
            logger.info(
                f'Exception from service {service}: {details}')
        return (service.name, results)

    async def _get_mentions(self, loop, entities: List[str], limit: int = 20) -> List[dict]:
        pub_collections = await asyncio.gather(*[TextMiningDeMultiplexer.wrap_get_mentions(loop, service, entities, limit=limit) for service in self.services])
        return pub_collections

    def get_mentions(self, entities: List[str], limit: int = 20) -> List[dict]:
        loop = asyncio.new_event_loop()
        try:
            results = loop.run_until_complete(
                self._get_mentions(loop, entities, limit=limit))
            loop.run_until_complete(loop.shutdown_asyncgens())
        finally:
            loop.close()
        return self.agg.aggregate_mentions(dict(results))

    #  ____ ____ ___    ____ ____    ____ ____ ____ _  _ ____ ____ ____ _  _ ____ ____ ____
    #  | __ |___  |     |    |  |    |  | |    |    |  | |__/ |__/ |___ |\ | |    |___ [__
    #  |__] |___  |     |___ |__|    |__| |___ |___ |__| |  \ |  \ |___ | \| |___ |___ ___]
    #
    @staticmethod
    async def wrap_get_co_occurrences(loop, service: 'TextMiningService', entity: str, limit: int = 20, types: List[str] = None) -> List[CoOccurrence]:
        results = []
        try:
            logger.info(f'Entity {entity} Service {service.name}')
            results = await loop.run_in_executor(None, partial(service.get_co_occurrences, entity, limit=limit, types=types))
        except TextMiningServiceOperationNotSupported:
            details = sys.exc_info()[0]
            logger.info(f'Exception from service {service}: {details}')
        except Exception:
            details = sys.exc_info()[0]
            logger.info(f'Exception from service {service}: {details}')
            logger.info(traceback.print_exc())
        return (service.name, results)

    async def _get_co_occurrences(self, loop, entity: str, limit: int = 20, types: List[str] = None) -> List[CoOccurrence]:
        entity_collections = await asyncio.gather(*[TextMiningDeMultiplexer.wrap_get_co_occurrences(loop, service, entity, limit=limit, types=types) for service in self.services])
        return entity_collections

    def get_co_occurrences(self, entity: str, limit: int = 20, types: List[str] = None) -> List[CoOccurrence]:
        loop = asyncio.new_event_loop()
        try:
            entity_collections = loop.run_until_complete(
                self._get_co_occurrences(loop, entity, limit=limit, types=types))
            loop.run_until_complete(loop.shutdown_asyncgens())
        finally:
            loop.close()
        return self.agg.aggregate_cooccurrences(dict(entity_collections))


if __name__ == "__main__":
    tmdm = TextMiningDeMultiplexer()
    logger.info('get mentions')
    results = tmdm.get_mentions(["DOID:2841", "DOID:10652", "DOID:10935"])
    print(json.dumps(results))
    print('get cooccurrences')
    results = tmdm.get_co_occurrences('DOID:2841')
    print(json.dumps(results))
