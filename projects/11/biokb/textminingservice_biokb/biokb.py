import logging
from typing import List

from SPARQLWrapper import SPARQLWrapper, JSON, POSTDIRECTLY
from SPARQLWrapper.SPARQLExceptions import QueryBadFormed

from textminingservice.TextMiningService import TextMiningService
from textminingservice.models.coocurrence import CoOccurrence
from textminingservice.models.publication import Publication
from textminingservice_biokb.utils import uri_to_entity_code, standardise_underscored_entity_code

logger = logging.getLogger(__name__)


class BioKBClientException(Exception):
    pass


class MalformedQueryException(BioKBClientException):
    pass


class BioKBService(TextMiningService):
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
            entity = standardise_underscored_entity_code(entity)
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
            pub = Publication(other_id=solr_id)
            values.append(pub)

        return values

    def get_co_occurrences(self, entity: str, limit: int = 20, types: List[str] = None) -> List[CoOccurrence]:

        if types is None:
            types = []

        entity_types_filter = ''
        if len(types) > 0:
            types_str = ', '.join((f'<{t}>' for t in types))
            entity_types_filter = f'FILTER (?e_type IN ({types_str}) )'

        entity = standardise_underscored_entity_code(entity)
        query = """
            select * where {
    
                select ?other_entity, (COUNT(*) AS ?count) where {
                    
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
                
                GROUP BY ?other_entity 

            } ORDER BY DESC(?count) LIMIT %LIMIT%
        """.replace('%ENTITY%', entity).replace('%LIMIT%', str(limit)).replace('%ENTITY_TYPE_FILTER%',
                                                                               entity_types_filter)
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
    bkb = BioKBService()
    print(bkb.get_co_occurrences('DOID:2841', types=[
        'http://lcsb.uni.lu/biokb#Disease']))
    print('')
    print(bkb.get_co_occurrences('DOID:2841'))
    print('')
    print(bkb.get_mentions(['DOID:2841', 'DOID:1205']))