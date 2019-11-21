from textminingservice.aggregator import TextMiningDeMultiplexer
from flask import Flask, request, abort
import json
from flask_cors import CORS


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
    tmdm = TextMiningDeMultiplexer()
    return json.dumps(tmdm.get_mentions(entities, limit=limit))
