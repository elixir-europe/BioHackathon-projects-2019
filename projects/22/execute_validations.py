import re
from os import listdir

import prettytable

import neo_utils


def run_validation_queries():
    queries = load_validation_queries()
    for q in queries:
        response = neo_utils.execute_query(q["query"])
        if len(response.data()) > 0:
            q["status"] = "Failed"
        else:
            q["status"] = "Passed"

    return queries


def load_validation_queries():
    queries = []
    files = listdir("./validation_docs")
    for file in files:
        with open("./validation_docs/" + file, "r") as validation_file:
            query = extract_query(validation_file.read())
            query_object = {
                "file": file,
                "query": query,
                "status": ""
            }
            queries.append(query_object)

    return queries


def extract_query(validation_file_text):
    query = re.search(r'\[source,cypher\]\n----(.*?)----', validation_file_text, re.DOTALL)[1]
    return query


def main():
    print("Running validation queries")
    results = run_validation_queries()

    result_table = prettytable.PrettyTable(["File", "Query", "Result"])
    result_table.hrules = prettytable.ALL
    for r in results:
        result_table.add_row([r["file"], r["query"].strip(), r["status"]])

    print(result_table)


if __name__ == "__main__":
    main()
