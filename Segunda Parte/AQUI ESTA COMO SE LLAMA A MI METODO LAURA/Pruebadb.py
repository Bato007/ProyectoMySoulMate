from neo4j import GraphDatabase
import DB

db = GraphDatabase.driver("bolt://localhost:7687", auth = ("neo4j", "12345"), encrypted = False)



session = db.session()
q1 = "MATCH (x) return (x)"

nodes = session.run(q1)

nodes = list(nodes)

DB.agregarDatos("Harry Styles", "Sign of the Times", "Cancion 2", "Cancion 3", "Pop", "Soul", "Jazz", "2000", "2005", "2018")



for node in nodes:
    print(node)