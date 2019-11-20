import os

from fastapi import FastAPI
# from fastapi_contrib.pagination import Pagination
from flask_paginate import Pagination
from flask import request

from web_server.sparql_wrapper import execute_query, get_properties, get_total_papers
from web_server.neo4j_wrapper import execute_cypher

app = FastAPI()

@app.get('/api/v1/property')
def get_property():
    return get_properties()


@app.get('/api/v1/neo4j')
def query(doi: str = None):
    res = execute_cypher(doi)
    return res


@app.get('/api/v1/query')
def query(q: str = None, page: int = 1):
    res = execute_query({"q": q})
    #pagination = Pagination(
    #page=page, page_parameter=page, per_page_parameter=10, found=len(res), total=get_total_papers(),
    #record_name='papers', format_total=True, format_number=True,
    #search=True, bs_version=4)
    #res = list(res)[(int(page) * 10 - 10):(int(page) * 10)]
    return res 

#if __name__ == '__main__':
#    host = os.environ.get('FLASK_HOST', '127.0.0.1')
#    app.run(host=host, debug=True)
