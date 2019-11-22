neo4j stop

rm -r /usr/local/var/neo4j/
neo4j-admin import \
    --mode=csv \
    --nodes neo4j_nodes.csv \
    --relationships neo4j_edges.csv

neo4j start
