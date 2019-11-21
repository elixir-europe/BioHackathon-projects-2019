import logging
import datetime
from typing import List, Set, DefaultDict
from collections import defaultdict

import itertools
import requests
import json
import numpy as np

from textminingservice.TextMiningService import TextMiningService
from textminingservice.models.cooccurrence import CoOccurrence
from textminingservice.models.publication import Publication
from textminingservice.exceptions import TextMiningServiceOperationNotSupported

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PMC_Europe_Service(TextMiningService):
    """[summary]

    Arguments:
        TextMiningService {[type]} -- [description]
    """
    MAX_PAGE_SIZE = 500
    BASE_URL = 'https://www.ebi.ac.uk'
    MENTION_URL = BASE_URL + \
        '/europepmc/annotations_api/annotationsByEntity?entity={}&filter={}&format={}&cursorMark={}&pageSize={}'

    def __init__(self):
        super().__init__('PCM Europe',
                         'This client communicates with PCM Europe API.')

    def _get_single_entity_mentions(self, entity: str, pageSize: int = None):
        """
        Generator that yields each article and article id that mentions the given entity
        See https://europepmc.org/AnnotationsApi!/annotations45api45controller/getAnnotationsArticlesByEntityUsingGET

        The articles come up sorted by number of mentions
        """
        if pageSize is None:
            pageSize = PMC_Europe_Service.MAX_PAGE_SIZE

        prevCursorMark = -1
        cursorMark = 0
        counter = 0
        while cursorMark != prevCursorMark:
            url = PMC_Europe_Service.MENTION_URL.format(
                entity, 1, 'ID_LIST', cursorMark, pageSize)
            logger.info(
                f'{datetime.datetime.now()} Getting {counter} to {counter+pageSize}')
            results = requests.get(url)
            assert results.ok
            logger.info(f'{datetime.datetime.now()} Ok')
            data = json.loads(results.content.decode().strip())
            prevCursorMark = cursorMark
            cursorMark = data['nextCursorMark']
            for article in data['articles']:
                counter += 1
                yield article, article['extId']

    def _incremental_intersection(self, entity: str, white_list: DefaultDict[str, float] = None):
        """Takes the given entity and returns every article with an ID contained in the given white list as well as a new white list with the new ids and recalculated scores.
        The score is the normalized position. (1-pos/length) giving more importance to the first article.
        The articles are given my PMC Europe sorted by the number of occurrences.

        The returned white list will be smaller or equal in size to the given white list.
        The scores are added up to the previous ones.
        """

        if white_list is None:
            white_list = defaultdict(float)

        new_article_list = []
        new_scores = []
        new_ids = []
        index = 0
        for article, article_id in self._get_single_entity_mentions(entity):
            index += 1
            # if no white list, keep all, otherwise, only those in white_list
            if len(white_list) == 0 or article_id in white_list:
                new_article_list.append(article)
                new_scores.append(index)
                new_ids.append(article_id)

        new_scores = 1-np.array(new_scores)/index  # normalize position score
        new_white_list = dict(zip(new_ids, new_scores))
        # update scores of the intersection
        for id in new_ids:
            new_white_list[id] += white_list[id]

        return new_article_list, new_white_list

    def get_mentions(self, entities: List[str], limit: int = 20) -> List[Publication]:
        if len(entities) == 1:
            pageSize = min(limit+1, PMC_Europe_Service.MAX_PAGE_SIZE)
            generator = self._get_single_entity_mentions(
                entities[0], pageSize=pageSize)
            publications = []
            for article, _ in generator:
                if len(publications) == limit:
                    return publications
                else:
                    publications.append(Publication(
                        pm_id=article['extId'], pmc_id=article['pmcid']))
        else:
            raise TextMiningServiceOperationNotSupported
            # once PMC is fast enough to deal with multiple entities, use either the following line
            # or _get_mentions_for_single_entity which can also be used with multiple entities
            # return self._get_mentions_for_multiple_entities(entities, limit=limit)

    def _get_mentions_for_multiple_entities(self, entities: List[str], limit: int = 20) -> List[Publication]:
        """
        Method for multiple entities retrieval. It's slow but a bit faster than _get_mentions_for_single_entity if there is a limit.
        """
        entities = list(map(str.lower, entities))
        first_entity = entities[0]
        rest_of_entities = entities[1:]

        if len(rest_of_entities) == 0:
            pageSize = min(PMC_Europe_Service.MAX_PAGE_SIZE, limit)
        else:
            pageSize = PMC_Europe_Service.MAX_PAGE_SIZE

        prevCursorMark = -1
        cursorMark = 0
        total_counter = 0
        yielded_counter = 0
        publications = []
        scores = []
        while cursorMark != prevCursorMark and len(publications) < limit:
            url = PMC_Europe_Service.MENTION_URL.format(
                first_entity, 0, 'JSON', cursorMark, pageSize)
            logger.info(
                f'{datetime.datetime.now()} Getting {total_counter} to {total_counter+pageSize}')
            results = requests.get(url)
            assert results.ok
            logger.info(f'{datetime.datetime.now()} Ok')
            data = json.loads(results.content.decode().strip())
            prevCursorMark = cursorMark
            cursorMark = data['nextCursorMark']
            for article in data['articles']:
                bool_table = dict(
                    zip(rest_of_entities, [0]*len(rest_of_entities)))
                total_counter += 1
                for annotation in article['annotations']:
                    other_entity = annotation['exact'].lower()
                    # check if this entity is what we look for
                    if other_entity in bool_table:
                        bool_table[other_entity] += 1
                # if the article includes all entities, then
                if all(bool_table.values()):
                    yielded_counter += 1
                    pub = Publication(pm_id=article_id,
                                      pmc_id=article['pmcid'])
                    publications.append(pub)
                    scores.append(sum(bool_table.values()))

        publications = np.array(publications)
        scores = np.array(scores)
        inds = scores.argsort()[::-1]
        return publications[inds]

    def _get_mentions_for_single_entity(self, entities: List[str], limit: int = 20) -> List[Publication]:
        """
        This method returns a list of publications sorted by importance.
        Since PMC Europe sorts the publications based on the number of occurrences,
         this new score could be seen as the degree of co-occurrence.

        It works well for single entity pub mention retrieval.
        Right now this does not work well for multiple entities because the pageSize is too small and PMC resource is too slow, hence the mentions retrieval time is too slow.
        """
        white_list = None
        article_list = []
        for entity in entities:
            article_list, white_list = self._incremental_intersection(
                entity, white_list=white_list)
        # last iteration contains the final intersection
        scores = []
        publications = []
        for article in article_list:
            article_id = article['extId']
            pub = Publication(pm_id=article_id, pmc_id=article['pmcid'])
            publications.append(pub)
            scores.append(white_list[article_id])

        publications = np.array(publications)
        scores = np.array(scores)
        inds = scores.argsort()[::-1]
        return publications[inds][:limit]

    def get_co_occurrences(self, entity: str, limit: int = 20, types: List[str] = None) -> List[CoOccurrence]:
        """Returns a list of co-occurrences from a given entity
        """
        raise TextMiningServiceOperationNotSupported


if __name__ == "__main__":
    pmc = PMC_Europe_Service()
    print(datetime.datetime.now())

    print('get mentions for single entity PRDM1')
    for pub in pmc.get_mentions(['PRDM1']):
        print(pub)

    print(datetime.datetime.now())
    # right now it raises TextMiningServiceOperationNotSupported
    # print('get mentions for multiple entities PRDM1, GFP')
    # for pub in pmc.get_mentions(['PRDM1', 'GFP']):
    #     print(pub)
    # print(datetime.datetime.now())
