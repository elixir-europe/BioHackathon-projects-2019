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
    if len(entities) == 0:
        abort(400)
    limit = request.args.get('limit', default=20, type=int)
    logger.info(f'parameters. Entities {entities} limit: {limit}')
    tmdm = TextMiningDeMultiplexer()
    format = request.args.get('format')
    results = tmdm.get_mentions(entities, limit=limit)
    if format == 'cytoscape':
        return jsonify(export_aggregated_mentions_cytoscape(entities, results))
    else:
        return jsonify(results)
