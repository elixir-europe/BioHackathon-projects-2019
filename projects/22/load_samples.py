import json

from neo4j import GraphDatabase
from decouple import config


class LoadSamples(object):

    def __init__(self, _uri, _user, _password, _json_path):
        self.json_path = _json_path
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
                    print(record['accession'])
            # greeting = session.write_transaction(self._create_biosample, id)

    @staticmethod
    def _create_biosample(tx, _id):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", id=_id)

    def clear_graph(self):
        # self._driver.delete_all()
        pass


if __name__ == "__main__":
    uri = config('URI')
    user = config('USERNAME')
    password = config('PASSWORD')
    json_path = config('JSON_FILE_PATH')
    load_samples_obj = LoadSamples(uri, user, password, json_path)
    load_samples_obj.load_biosamples_to_database()
