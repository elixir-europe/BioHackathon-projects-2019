import json
from collections import defaultdict
from typing import List, Dict

from textminingservice_biokb.biokb import BioKBService
from textminingservice_jensenlab.jensenlabservice import JensenLabService
from textminingservice_pmc_europe.pmc_europe import PMC_Europe_Service

from textminingservice.models.cooccurrence import CoOccurrence
from textminingservice.models.publication import Publication


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

    def get_mentions(self, entities: List[str], limit: int = 20) -> List[dict]:
        pub_collections = {}

        for service in self.services:
            try:
                results = service.get_mentions(entities, limit=limit)
            except Exception:
                results = []
            pub_collections[service.name] = results
        return self.agg.aggregate_mentions(pub_collections)

    def get_co_occurrences(self, entity: str, limit: int = 20, types: List[str] = None) -> List[CoOccurrence]:

        entity_collections = {}

        for service in self.services:
            try:
                results = service.get_co_occurrences(
                    entity, limit=limit, types=types)
            except Exception:
                results = []
            entity_collections[service.name] = results

        return self.agg.aggregate_cooccurrences(entity_collections)


if __name__ == "__main__":
    tmdm = TextMiningDeMultiplexer()
    print('get mentions')
    results = tmdm.get_mentions(['DOID:2841'])
    print(json.dumps(results))
    print('get cooccurrences')
    results = tmdm.get_co_occurrences('DOID:2841')
    print(json.dumps(results))
