#!/bin/bash

systemctl stop neo4j

cd /srv/neo4j/data

rm -r /srv/neo4j/data/databases
neo4j-admin import \
--mode=csv \
--nodes /home/idefix/neo4j_nodes.csv \
--relationships /home/idefix/neo4j_edges.csv

chown neo4j:neo4j --recursive databases

systemctl start neo4j
journalctl -f
