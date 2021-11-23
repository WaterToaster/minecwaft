import neo4j
from neo4j import GraphDatabase,basic_auth

uri = "neo4j://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "Passw0rd"))
session = driver.session()
q1 = 'MATCH (n) RETURN n'
nodes = session.run(q1)
for node in nodes:
    print (node)