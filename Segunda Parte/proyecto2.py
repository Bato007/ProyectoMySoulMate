from neo4j import GraphDatabase

# Autores:
# Martin Amado 19020
# Andrea Amaya 19357
# Brandon Hernández 19376
# Laura Tamath 19365
# 
# Fecha: 24/05/2020
# Nombre: Neo4j_DB.py

# Se abre la secion de Neo4j
db = GraphDatabase.driver("bolt://localhost:7687",
                          auth =("neo4j","1234"), encrypted = False)
session = db.session()

# Obtiene los nombres de todos los artistas
# pre: La base de datos debe de tener al menos un dato,
#      debe de ser una 'Cancion' o un 'Artista'
# Param: El nombre del label del nodo
# Return: Una lista con todos los nombres de artistas que hay en la base de datos
def get_node_name(node_type):
    temp = [] # Guarda los nombres de los artistas
    q1 = "MATCH (x:%s) RETURN x" %node_type
    nodes = session.run(q1)
    nodes = list(nodes)
 
    # Metiendo los nombres al 
    for node in nodes:
        temp.append(dict(dict(node)['x'])['nombre'])
    return temp
    
def search_node(searched_node):
    q1 = "MATCH (x {nombre:'%s'}) RETURN x" %searched_node
    node = session.run(q1)
    print(node) # En proceso
   
aux = get_node_name('Artista')
aux2 = get_node_name('Cancion')
search_node('Lorde')
