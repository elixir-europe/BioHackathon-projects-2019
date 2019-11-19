import json

from neo4j import GraphDatabase
from decouple import config


class LoadSamples(object):

    def __init__(self, _uri, _user, _password, _json_path):
        self.json_path = _json_path
        self.accessions = list()
        # Create driver instance and clean database
        self._driver = GraphDatabase.driver(_uri, auth=(_user, _password))
        self.clear_graph()

    def close(self):
        self._driver.close()

    def load_biosamples_to_database(self):
        with self._driver.session() as session:
            with open(self.json_path) as json_file:
                data = json.load(json_file)
                for record in data:
                    self.accessions.append(record['accession'])
                    if 'material' in record['characteristics']:
                        session.write_transaction(
                            self._create_biosample, record['accession'],
                            record['characteristics']['material'][0]['text'],
                            'FAANG')
                    else:
                        session.write_transaction(
                            self._create_biosample, record['accession'],
                            'Unknown', 'FAANG')

    def create_relationships(self):
        with self._driver.session() as session:
            with open(self.json_path) as json_file:
                data = json.load(json_file)
                for record in data:
                    for relationship in record['relationships']:
                        if relationship['source'] not in self.accessions:
                            session.write_transaction(
                                self._create_biosample, relationship['source'],
                                'Unknown', 'not FAANG')
                        if relationship['target'] not in self.accessions:
                            session.write_transaction(
                                self._create_biosample, relationship['target'],
                                'Unknown', 'not FAANG')

    @staticmethod
    def _create_biosample(tx, _id, _material, _project):
        tx.run("CREATE (b:Biosample) SET b.accession = $accession, "
               "b.material = $material, b.project = $project ",
               accession=_id, material=_material, project=_project)

    def clear_graph(self):
        with self._driver.session() as session:
            session.write_transaction(self._delete_all)

    @staticmethod
    def _delete_all(tx):
        tx.run("MATCH (n) DETACH DELETE n")


if __name__ == "__main__":
    uri = config('URI')
    user = config('USERNAME')
    password = config('PASSWORD')
    json_path = config('JSON_FILE_PATH')
    load_samples_obj = LoadSamples(uri, user, password, json_path)
    load_samples_obj.load_biosamples_to_database()
    load_samples_obj.create_relationships()

