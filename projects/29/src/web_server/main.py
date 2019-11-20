import os

from fastapi import FastAPI
# from fastapi_contrib.pagination import Pagination

from pydantic import BaseModel

from web_server.sparql_wrapper import execute_query, get_total_papers
from web_server.neo4j_wrapper import execute_cypher, test, get_properties, execute_cypher_simple

class Query(BaseModel):
    category: str
    operator: str
    value: str

test()

app = FastAPI()

@app.get('/api/v1/property')
def get_property():
    return get_properties()


@app.get('/api/v1/doi')
def query(doi: str = None):
    res = execute_cypher_simple(doi)
    return res


class Query(BaseModel):
    q: list = []

@app.post('/api/v1/query')
def query(q: Query):
    res = execute_cypher(q)
    return res

#@app.get('/api/v1/query')
#def query(q: str = None, page: int = 1):
#    res = execute_query({"q": q})
    #pagination = Pagination(
    #page=page, page_parameter=page, per_page_parameter=10, found=len(res), total=get_total_papers(),
    #record_name='papers', format_total=True, format_number=True,
    #search=True, bs_version=4)
    #res = list(res)[(int(page) * 10 - 10):(int(page) * 10)]
#    return res 



#if __name__ == '__main__':
#    host = os.environ.get('FLASK_HOST', '127.0.0.1')
#    app.run(host=host, debug=True)
