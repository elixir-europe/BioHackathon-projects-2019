biosamples_url = "https://www.ebi.ac.uk/biosamples/samples"
output_file = "samples.json"
page_size = 100
request_timeout = 50
neo4j_url = "bolt://localhost:7687"
neo4j_user = "neo4j"
neo4j_password = "neo5j"

example_sample = {
    "accession": "SAMEA103886111",
    "characteristics": {
        "material": [
            {
                "text": "specimen from organism",
                "ontologyTerms": [
                    "http://purl.obolibrary.org/obo/OBI_0001479"
                ]
            }
        ]
    },
    "relationships": [
        {
            "source": "SAMEA103886111",
            "type": "derived from",
            "target": "SAMEA103886123"
        },
        {
            "source": "SAMEG318793",
            "type": "has member",
            "target": "SAMEA103886111"
        }
    ],
    "externalReferences": [
        {
            "url": "http://www.ebi.ac.uk/ena/data/view/SAMEA103886111"
        }
    ]
}

relationships = {"derived from": 'DERIVED_FROM'}
