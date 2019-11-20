import logging
from typing import List, Set, DefaultDict
from collections import defaultdict

import itertools
import requests
import json
import numpy as np

from textminingservice.TextMiningService import TextMiningService
from textminingservice.models.coocurrence import CoOccurrence
from textminingservice.models.publication import Publication

logger = logging.getLogger(__name__)


class PMC_Europe_Service(TextMiningService):
    """[summary]

    Arguments:
        TextMiningService {[type]} -- [description]
    """
    MAX_PAGE_SIZE = 8
    BASE_URL = 'https://www.ebi.ac.uk'
    MENTION_URL = BASE_URL + \
        '/europepmc/annotations_api/annotationsByEntity?entity={}&filter={}&format={}&cursorMark={}&pageSize={}'

    def __init__(self):
        super().__init__('PCM Europe',
                         'This client communicates with PCM Europe API.')

    def _get_single_entity_mentions(self, entity: str):
        """
        Generator that yields each article and article id that mentions the given entity

        See https://europepmc.org/AnnotationsApi#!/annotations45api45controller/getAnnotationsArticlesByEntityUsingGET

        The articles come up sorted by number of mentions
        """
        prevCursorMark = -1
        cursorMark = 0
        counter = 0
        while cursorMark != prevCursorMark:
            url = PMC_Europe_Service.MENTION_URL.format(
                entity, 1, 'ID_LIST', cursorMark, PMC_Europe_Service.MAX_PAGE_SIZE)
            print(f'Get {counter}')
            results = requests.get(url)
            assert results.ok
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
        """
        This method returns a list of publications sorted by importance.
        Since PMC Europe sorts the publications based on the number of occurrences, 
         this new score could be seen as the degree of co-occurrence.
        """
        white_list = None
        article_list = []
        for entity in entities:
            article_list, white_list = self._incremental_intersection(
                entity, white_list=white_list)
            print(article_list)
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
        return publications[inds]

    def get_co_occurrences(self, entity: str, limit: int = 20, types: List[str] = None) -> List[CoOccurrence]:
        pass


if __name__ == "__main__":
    pmc = PMC_Europe_Service()
    for pub in pmc.get_mentions(['P53', 'PRDM1']):
        print(pub)
