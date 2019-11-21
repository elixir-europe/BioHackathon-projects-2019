from textminingservice_biokb.biokb import BioKBService
from textminingservice_jensenlab.jensenlabservice import JensenLabService
from textminingservice_pmc_europe.pmc_europe import PMC_Europe_Service
from textminingservice.models.cooccurrence import CoOccurrence
from textminingservice.models.publication import Publication
from typing import List, Dict, Any
from collections import defaultdict
import json


class Aggregator():
    def __init__(self):
        pass

    def aggregate_mentions(self, pub_collections: Dict):
        pub_dict = defaultdict(dict)
        for service, pub_lst in pub_collections.items():
            print(service)
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


class TextMiningDeMultiplexer():
    def __init__(self):
        biokb = BioKBService()
        jensen = JensenLabService()
        pmc = PMC_Europe_Service()
        self.services = [biokb, jensen, pmc]
        self.agg = Aggregator()

    def get_mentions(self, entities: List[str], limit: int = 20) -> List[Publication]:
        pub_collections = {}

        for service in self.services:
            try:
                results = service.get_mentions(entities, limit=limit)
            except Exception:
                results = []
            pub_collections[service.name] = results
        return self.agg.aggregate_mentions(pub_collections)


if __name__ == "__main__":
    tmdm = TextMiningDeMultiplexer()
    results = tmdm.get_mentions(['DOID:2841'])
    print(json.dumps(results))
