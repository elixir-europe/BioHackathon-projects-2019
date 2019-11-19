import logging

from biokb.biokb import BioKBService
from jensenLabService.jensenLabService import JensenLabService

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    text_mining_services = [JensenLabService(), BioKBService()]
    for text_mining_service in text_mining_services:
        print("Using service {}".format(text_mining_service.name))
        publications = text_mining_service.get_mentions(
            ["DOID:10652", "DOID:10935"], limit=100)
        print(", ".join([str(p) for p in publications]))
