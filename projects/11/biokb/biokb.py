from typing import List
from interface.TextMiningService import TextMiningService
from models.publication import Publication
from models.coocurrence import CoOccurrence
from biokb.utils import uri_to_code

from SPARQLWrapper import SPARQLWrapper, JSON
from SPARQLWrapper.SPARQLExceptions import EndPointNotFound, EndPointInternalError, QueryBadFormed

import logging
logger = logging.getLogger(__name__)

class BioKBClientException(Exception):
    pass


class MalformedQueryException(BioKBClientException):
    pass


class BioKBservice(TextMiningService):
    def __init__(self, sparql_url="https://biokb.lcsb.uni.lu/sparql"):
        self.sparql = SPARQLWrapper(sparql_url)
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

        entity_subquery = ""
        for entity in entities:
            entity_subquery += f"?publication <http://lcsb.uni.lu/biokb#containsEntity> <http://lcsb.uni.lu/biokb/entities/{entity}> .\n"

        query = """
            select ?publication str(?solrId) as ?solrId where {{
                {} 
                ?publication <http://lcsb.uni.lu/biokb#solrId> ?solrId	.
            }} LIMIT {}
            """.format(entity_subquery, limit)

        results = self._run_sparql_query(query)
        values = []
        for result in results['results']['bindings']:
            solr_id = result['solrId']['value']
            publication_uri = result['publication']['value']
            values.append(
                {"solr_id": solr_id, "publication_uri": publication_uri})

        return values

    def get_co_occurrences(self, entity: str) -> List[CoOccurrence]:
        query = """
            select * where {
    
                select ?other_entity, (COUNT(*) AS ?count) where {
                    
                    ?s <http://lcsb.uni.lu/biokb#containsEntity> <http://lcsb.uni.lu/biokb/entities/%ENTITY%> .
                    ?s a  <http://lcsb.uni.lu/biokb#Publication> .
                    ?s <http://lcsb.uni.lu/biokb#containsEntity> ?other_entity .
                
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
                
                GROUP BY ?other_entity 

            } ORDER BY DESC(?count)
        """.replace('%ENTITY', entity)

        results = self._run_sparql_query(query)
        values = []
        values = []
        for result in results['results']['bindings']:
            entity_code = uri_to_code(result['other_entity']['value'])
            count       = int(result['count']['value'])
            co_occur    = CoOccurrence(entity_code, count)
            values.append(co_occur)
        return values
