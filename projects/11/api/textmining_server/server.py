from textminingservice.aggregator import TextMiningDeMultiplexer
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
def getMentions():
    entities = request.args.getlist('entity')
    if len(entities) == 0:
        abort(400)
    limit = request.args.get('limit', default=20, type=int)
    logger.info(f'parameters. Entities {entities} limit: {limit}')
    tmdm = TextMiningDeMultiplexer()
    return json.dumps(tmdm.get_mentions(entities, limit=limit))
