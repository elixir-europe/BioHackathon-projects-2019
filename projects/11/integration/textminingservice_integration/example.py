from textminingservice_biokb.biokb import BioKBService
from textminingservice_dummy.dummyService import DummyService
from textminingservice_jensenlab.jensenlabservice import JensenLabService

if __name__ == '__main__':
    text_mining_services = [DummyService(), BioKBService(), JensenLabService()]
    for text_mining_service in text_mining_services:
        print("Using service {}".format(text_mining_service.name))
        publications = text_mining_service.get_mentions(
            ["DOID:10652", "DOID:10935"], limit=100)
        print(", ".join([str(p) for p in publications]))
