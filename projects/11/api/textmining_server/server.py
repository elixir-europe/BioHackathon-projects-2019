import logging
import json
from flask import Flask, request, abort
from textminingservice.exporters.exporters import export_aggregated_mentions_cytoscape, export_aggregated_cooccurrences_cytoscape
from textminingservice.aggregator import TextMiningDeMultiplexer
from flask_cors import CORS
from flask import Flask, request, abort, jsonify


logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s.%(funcName)s @ %(name)s ::: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)
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
    results = tmdm.get_co_occurrences(entity, limit=limit, types=entity_types)
    format = request.args.get('format')
    if format == 'cytoscape':
        return jsonify(export_aggregated_cooccurrences_cytoscape(entity, results))
    else:
        return jsonify(results)


@app.route('/bulk/getCooccurrence/', methods=['GET', 'POST'])
def bulkGetCooccurrences():
    entities = request.args.getlist('entity')
    entities = [entity for entity in entities if entity != '']
    if len(entities) == 0:
        abort(400)
    limit = request.args.get('limit', default=20, type=int)
    entity_types = request.args.getlist('type', type=int)
    if len(entity_types) == 0:
        entity_types = None
    logger.info(
        f'Bulk getCooccurrences parameters. Entities {entities} limit: {limit} types: {entity_types}')
    tmdm = TextMiningDeMultiplexer()

    format = request.args.get('format')

    response = {}
    for entity in entities:
        results = tmdm.get_co_occurrences(
            entity, limit=limit, types=entity_types)
        if format == 'cytoscape':
            response[entity] = export_aggregated_cooccurrences_cytoscape(
                entity, results)
        else:
            response[entity] = results
    return jsonify(response)


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
