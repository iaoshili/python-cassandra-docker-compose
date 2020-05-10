#!/usr/local/bin/python3
import os

from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement

KEYSPACE = os.environ["CASSANDRA_KEYSPACE"]
cluster = Cluster([os.environ["CASSANDRA_IP_ADDRESS"]], port=9042)
session = cluster.connect(KEYSPACE, wait_for_all_pools=True)

query = SimpleStatement("""
    INSERT INTO mytable (thekey, col1, col2)
    VALUES (%(key)s, %(a)s, %(b)s)
    """, consistency_level=ConsistencyLevel.ONE)

prepared = session.prepare("""
    INSERT INTO mytable (thekey, col1, col2)
    VALUES (?, ?, ?)
    """)

for i in range(10):
    print("inserting row %d" % i)
    session.execute(query, dict(key="key%d" % i, a='a', b='b'))
    session.execute(prepared, ("key%d" % i, 'b', 'b'))
