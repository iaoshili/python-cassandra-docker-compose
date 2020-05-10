#!/usr/local/bin/python3
import os

from cassandra.cluster import Cluster

KEYSPACE = os.environ["CASSANDRA_KEYSPACE"]
cluster = Cluster([os.environ["CASSANDRA_IP_ADDRESS"]], port=9042)
session = cluster.connect()
print("creating keyspace...")
session.execute("""
    CREATE KEYSPACE IF NOT EXISTS %s
    WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '2' }
    """ % KEYSPACE)

cluster = Cluster([os.environ["CASSANDRA_IP_ADDRESS"]], port=9042)
session = cluster.connect(KEYSPACE, wait_for_all_pools=True)
print("creating table...")
session.execute("""
        CREATE TABLE IF NOT EXISTS mytable (
            thekey text,
            col1 text,
            col2 text,
            PRIMARY KEY (thekey, col1)
        )
        """)
