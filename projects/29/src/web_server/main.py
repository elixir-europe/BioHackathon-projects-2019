import os

from fastapi import FastAPI
from pydantic import BaseModel
from web_server.neo4j_wrapper import execute_cypher, test, get_properties, execute_cypher_simple, execute_cypher_update

class Query(BaseModel):
    q: list = []
    limit: int = 9

class DOIs(BaseModel):
    positive: list = []
    negative: list = []
    unvoted: list = []


# test()

app = FastAPI()

@app.get('/api/v1/property')
def get_property():
    return get_properties()


@app.get('/api/v1/doi')
def doi(doi: str = None):
    res = execute_cypher_simple(doi)
    return res


@app.post('/api/v1/query')
def query(q: Query):
    res = execute_cypher(q.q, q.limit)
    return res


@app.post('/api/v1/update')
def update(q: DOIs):
    res = execute_cypher_update(q)
    return res
