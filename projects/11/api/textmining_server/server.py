from flask import Flask, request, abort, jsonify
from flask_cors import CORS

from textminingservice.aggregator import TextMiningDeMultiplexer
from textminingservice.exporters.exporters import export_aggregated_mentions_cytoscape
from flask import Flask, request, abort
import json
from flask_cors import CORS
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)


@app.route('/ping')
def ping():
    return 'pong'


@app.route('/getMentions/', methods=['GET', 'POST'])
def get_mentions():
    entities = request.args.getlist('entity')
    entities = [entity for entity in entities if entity != '']
    if len(entities) == 0:
        abort(400)
    limit = request.args.get('limit', default=20, type=int)
    logger.info(f'getMentions parameters. Entities {entities} limit: {limit}')
    tmdm = TextMiningDeMultiplexer()
    format = request.args.get('format')
    results = tmdm.get_mentions(entities, limit=limit)
    if format == 'cytoscape':
        return jsonify(export_aggregated_mentions_cytoscape(entities, results))
    else:
        return jsonify(results)


@app.route('/getCooccurrence/<entity>', methods=['GET', 'POST'])
def getCooccurrences(entity: str):
    if entity == '':
        abort(400)
    limit = request.args.get('limit', default=20, type=int)
    entity_types = request.args.getlist('type', type=int)
    if len(entity_types) == 0:
        entity_types = None
    logger.info(
        f'getCooccurrences parameters. Entity {entity} limit: {limit} types: {entity_types}')
    tmdm = TextMiningDeMultiplexer()
    return jsonify(tmdm.get_co_occurrences(entity, limit=limit, types=entity_types))


# Type	entity type
# any > 0	Proteins of species with this NCBI tax id
# -1	chemicals
# -2	NCBI species taxonomy id (tagging species)
# -3	NCBI species taxonomy id (tagging proteins)
# -11	Wikipedia
# -21	GO biological process
# -22	GO cellular component
# -23	GO molecular function
# -24	GO other (unused)
# -25	BTO tissues
# -26	DOID diseases
# -27	ENVO environments
# -28	APO phenotypes
# -29	FYPO phenotypes
# -30	MPheno phenotypes
# -31	NBO behaviors
# -36	mammalian phenotypes
