from textminingservice.exporters.exporters import export_cooccurrences_cytoscape
from textminingservice_biokb.biokb import BioKBService
from textminingservice_jensenlab.jensenlabservice import JensenLabService

if __name__ == '__main__':
    entities = ["DOID:10584", "DOID:10935"]
    text_mining_services = [JensenLabService(), BioKBService()]
    for text_mining_service in text_mining_services:
        print("Using service {}".format(text_mining_service.name))
        # publications = text_mining_service.get_mentions(entities, limit=100)
        cooccurrences = text_mining_service.get_co_occurrences(entities[0], limit=100)
        # print(", ".join([str(p) for p in publications]))

    # json_cytoscape = export_mentions_cytoscape(entities, publications)
    json_cytoscape = export_cooccurrences_cytoscape(entities[0], cooccurrences)
    print(json_cytoscape)
