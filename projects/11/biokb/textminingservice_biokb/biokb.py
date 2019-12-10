import json
import logging
from typing import List

import requests
from SPARQLWrapper import SPARQLWrapper, JSON, POSTDIRECTLY
from SPARQLWrapper.SPARQLExceptions import QueryBadFormed

from textminingservice.TextMiningService import TextMiningService
from textminingservice.models.cooccurrence import CoOccurrence
from textminingservice.models.publication import Publication
from textminingservice_biokb.utils import uri_to_entity_code, standardise_underscored_entity_code, \
    reflect_type_to_biokb, standardise_entity_type

from textminingservice_biokb import logger


class BioKBClientException(Exception):
    pass


class MalformedQueryException(BioKBClientException):
    pass


class BioKBService(TextMiningService):
    SOLR_TRANSLATOR_URL = 'https://biokb.lcsb.uni.lu/api/solr-ids-to-publications'
    # ?solrIds=4b267858-bbde-11e5-9b9d-001a4ae51247&solrIds=593fa4e6-c87e-11e8-ac16-001a4a160176
    SPARQL_URL = 'https://biokb.lcsb.uni.lu/sparql'

    def __init__(self):
        self.sparql = SPARQLWrapper(BioKBService.SPARQL_URL)
        self.sparql.setRequestMethod(POSTDIRECTLY)
        super().__init__('BioKB',
                         'This client communicates with BioKB triple store and Publication Solr index.')

    def _run_sparql_query(self, sparql_query):
        try:
            self.sparql.setQuery(sparql_query)
            self.sparql.setReturnFormat(JSON)
            results = self.sparql.query().convert()
            return results
        except QueryBadFormed as e:
            logger.error(e)
            raise MalformedQueryException(e)

    def get_mentions(self, entities: List[str], limit: int = 20) -> List[Publication]:
        logger.info('get mentions')
        entity_subquery = ""
        for entity in entities:
            entity = standardise_underscored_entity_code(entity)
            entity_subquery += f"?publication <http://lcsb.uni.lu/biokb#containsEntity> <http://lcsb.uni.lu/biokb/entities/{entity}> .\n"

        query = """
            select ?publication str(?solrId) as ?solrId where {{
                {}
                ?publication <http://lcsb.uni.lu/biokb#solrId> ?solrId	.
            }} LIMIT {}
            """.format(entity_subquery, limit)
        results = self._run_sparql_query(query)
        solr_ids = set()
        for result in results['results']['bindings']:
            solr_id = result['solrId']['value']
            solr_ids.add(solr_id)

        # translate ids
        response = requests.post(BioKBService.SOLR_TRANSLATOR_URL,
                                 data={'solrIds': solr_ids})
        logger.info(
            f'BioKB {entities} {limit} ({len(solr_ids)}): {response.url}')
        assert response.ok
        data = json.loads(response.content.decode().strip())
        publications = []
        for pub in data['publications']:
            title = pub.get('title', None)
            journal_title = pub.get('journal_title', None)
            doi = pub.get('doi', None)
            pm_id = pub.get('pubmed_id', None)
            pmc_id = pub.get('pmc_id', None)
            other_id = pub['id']
            year = pub.get('year', None)
            p = Publication(title=title,
                            journal_title=journal_title,
                            doi=doi,
                            pm_id=pm_id,
                            pmc_id=pmc_id,
                            other_id=other_id,
                            year=year)
            publications.append(p)
        return publications

    def get_co_occurrences(self, entity: str, limit: int = 20, types: List[str] = None) -> List[CoOccurrence]:

        if types is None:
            types = []

        # translate types, keep only those != None
        new_types = []
        for t in types:
            new_t = reflect_type_to_biokb(t)
            if new_t is not None:
                new_types.append(new_t)
        types = new_types

        entity_types_filter = ''
        if len(types) > 0:
            types_str = ', '.join((f'<{t}>' for t in types))
            entity_types_filter = f'FILTER (?e_type IN ({types_str}) )'

        entity = standardise_underscored_entity_code(entity)
        query = """
            select * where {
    
                select ?other_entity, ?e_type, (COUNT(*) AS ?count) where {
                    
                    ?s <http://lcsb.uni.lu/biokb#containsEntity> <http://lcsb.uni.lu/biokb/entities/%ENTITY%> .
                    ?s a  <http://lcsb.uni.lu/biokb#Publication> .
                    ?s <http://lcsb.uni.lu/biokb#containsEntity> ?other_entity .
                    ?other_entity a ?e_type .
                    %ENTITY_TYPE_FILTER%
                
                    OPTIONAL {?ss rdfs:subClassOf ?other_entity} .
                
                    FILTER (!bound(?ss)) .
                    FILTER(?other_entity != <http://lcsb.uni.lu/biokb/entities/%ENTITY%>) .
                    
                    OPTIONAL {
                        ?other_entity owl:sameAs ?o_original .
                    } .
                    
                    OPTIONAL {
                        ?other_entity a <http://lcsb.uni.lu/biokb#Protein> .
                        ?other_entity owl:sameAs ?ensembl_protein .
                    }
                }
                
                GROUP BY ?other_entity ?e_type
            } ORDER BY DESC(?count) LIMIT %LIMIT%
        """.replace('%ENTITY%', entity).replace('%LIMIT%', str(limit)).replace('%ENTITY_TYPE_FILTER%',
                                                                               entity_types_filter)
        results = self._run_sparql_query(query)
        values = []
        for result in results['results']['bindings']:
            entity_code = uri_to_entity_code(result['other_entity']['value'])
            count = int(result['count']['value'])
            entity_type = result['e_type']['value']
            entity_type = standardise_entity_type(entity_type)
            co_occur = CoOccurrence(entity_code, count, entity_type)
            values.append(co_occur)
        return values


if __name__ == "__main__":
    bkb = BioKBService()
    logger.info('Main BioKB')
    print(bkb.get_mentions(["DOID:2841"]))
    print(bkb.get_mentions(["GO:0002206"]))
    print(bkb.get_mentions(["DOID:10652", "DOID:10935"]))
    print('')
    print(bkb.get_co_occurrences('DOID:2841', types=[-3]))
    print('')
    print('test biokb protein and chemical co-occurrences')
    print(bkb.get_co_occurrences('DOID:2841', types=[-3, -1]))
