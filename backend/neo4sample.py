from neo4j import GraphDatabase
from dotenv import load_dotenv
from os import getenv


class Neo4JPlayground(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    @staticmethod
    def _perist_drugbank_query(tx):
        result = tx.run(
            'LOAD  CSV  WITH  HEADERS '
            'FROM "file:///drugbank.csv" AS row '
            'FIELDTERMINATOR ";" '
            'WITH  row  WHERE  row.Name IS NOT  NULL '
            'MERGE (m:Molecule {name: row.Name, description: coalesce(row.Description , "No  description")}) '
            'MERGE (p:Molecule {name: coalesce(row.Direct_parent , "No  parent")}) '
            'MERGE (m) -[:CHILD_OF]->(p) '
            'MERGE (k:Kingdom {name: coalesce(row.Kingdom , "No  kingdom")}) '
            'MERGE (m) -[: IN_KINGDOM]->(k) '
            'MERGE (supc:Class {name: coalesce(row.Superclass , "No  super c")}) '
            'MERGE (m) -[:IS_SUB_C]->(supc) '
            'MERGE (c:Class {name: coalesce(row.Class , "No class")}) '
            'MERGE (m) -[:IS_CLASS]->(c) '
            'MERGE (subc:Class {name: coalesce(row.Subclass , "No sub c")}) '
            'MERGE (m) -[: IS_SUPER_C]->(subc);',
        )
        return result.single()

    def persist_drugbank(self):
        with self._driver.session() as session:
            result = session.write_transaction(self._perist_drugbank_query)
            print(result)


if __name__ == "__main__":
    load_dotenv()
    neo = Neo4JPlayground(getenv("BOLT_URL"), getenv("USERNAME"), getenv("PASSWORD"))
    neo.persist_drugbank()
