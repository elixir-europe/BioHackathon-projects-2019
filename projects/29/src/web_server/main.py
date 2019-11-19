import os

from fastapi import FastAPI
#from fastapi_contrib import Pagination
from flask_paginate import Pagination, get_page_parameter

from web_server.neo4j_wrapper import execute_query

app = FastAPI()

@app.get('/api/v1/property')
def get_property():
    return get_properties()


@app.get('/api/v1/query')
def query(doi: str = None):
    res = execute_query(doi)
    return res


#if __name__ == '__main__':
#    host = os.environ.get('FLASK_HOST', '127.0.0.1')
#    app.run(host=host, debug=True)
