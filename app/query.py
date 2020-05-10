#!/usr/local/bin/python3
import os

from cassandra.cluster import Cluster

KEYSPACE = os.environ["CASSANDRA_KEYSPACE"]
cluster = Cluster([os.environ["CASSANDRA_IP_ADDRESS"]], port=9042)
session = cluster.connect(KEYSPACE, wait_for_all_pools=True)

for row in session.execute("SELECT * FROM mytable"):
    print(row)
