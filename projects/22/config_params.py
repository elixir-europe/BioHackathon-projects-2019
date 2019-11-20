from decouple import config


class Configurations:
    def __init__(self):
        self.biosamples_url = config('biosamples_url', default='https://www.ebi.ac.uk/biosamples/samples')
        self.data_file = config('data_file', default='data/samples.json')
        self.neo4j_url = config('neo4j_url', default='bolt://localhost:7687')
        self.neo4j_user = config('neo4j_user', default='neo4j')
        self.neo4j_password = config('neo4j_password', default='neo5j')
