from typing import List
from interface.TextMiningService import TextMiningService
from models.publication import Publication
from models.coocurrence import CoOccurrence
from utils import uri_to_entity_code, standarise_underscored_entity_code

from SPARQLWrapper import SPARQLWrapper, JSON, POSTDIRECTLY
from SPARQLWrapper.SPARQLExceptions import EndPointNotFound, EndPointInternalError, QueryBadFormed

import logging
logger = logging.getLogger(__name__)


class BioKBClientException(Exception):
    pass


class MalformedQueryException(BioKBClientException):
    pass


class BioKBservice(TextMiningService):
    def __init__(self, sparql_url="http://10.240.6.71:8890/sparql"):
        self.sparql = SPARQLWrapper(sparql_url)
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

        entity_subquery = ""
        for entity in entities:
            entity = standarise_underscored_entity_code(entity)
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

    def get_co_occurrences(self, entity: str, limit: int = 20) -> List[CoOccurrence]:
        entity = standarise_underscored_entity_code(entity)
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

            } ORDER BY DESC(?count) LIMIT %LIMIT%
        """.replace('%ENTITY%', entity).replace('%LIMIT%', str(limit))
        results = self._run_sparql_query(query)
        values = []
        values = []
        for result in results['results']['bindings']:
            entity_code = uri_to_entity_code(result['other_entity']['value'])
            count = int(result['count']['value'])
            co_occur = CoOccurrence(entity_code, count)
            values.append(co_occur)
        return values


if __name__ == "__main__":
    bkb = BioKBservice()
    print(bkb.get_co_occurrences('DOID:2841'))
    print('')
    print(bkb.get_mentions(['DOID:2841', 'DOID:1205']))
