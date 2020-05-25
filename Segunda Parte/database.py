from neo4j import GraphDatabase
import re
import random

# Autores:
# Martin Amado 19020
# Andrea Amaya 19357
# Brandon Hernández 19376
# Laura Tamath 19365
# 
# Fecha: 24/05/2020
# Nombre: database.py

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
   
#Params-> generos que le gustan
#Return-> cancion aleatoria
def song_recommendation_genre(genre1, genre2, genre3):
    genre_recommendations = []
    genre_recommendations = doing_genre_rec(genre1, genre_recommendations) #Realizando recomendacion genero 1
    genre_recommendations = doing_genre_rec(genre2, genre_recommendations) #Realizando recomendacion genero 2
    genre_recommendations = doing_genre_rec(genre3, genre_recommendations) #Realizando recomendacion genero 3
    
    random_artist = random.randrange(len(genre_recommendations)) #Generando artista al azar
    artist = genre_recommendations[random_artist] #Eligiendo artista
    
    #Buscando artista en la base
    q1 = "MATCH (Artista{nombre:'%s'}) - [:PERFORMS] - (Cancion) Return Cancion.nombre" %artist
    nodes = session.run(q1)
    nodes = list(nodes)
    
    #Generando cancion aleatoria del artista
    random_song = random.randrange(len(nodes))
    song_result = re.split("[']",str(nodes[random_song])) #Se separa por apostrofe
    
    #Retornando cancion - artista
    return song_result[1] + " - " + artist

#Params-> genero, lista de artistas generados por genero
#Return-> lista de artistas generados por genero
def doing_genre_rec(genre, genre_recommendations):
    #Buscando en la base por genero
    q1 = "MATCH (n)-[:WRITES]-(Genero{name:'%s'}) return n.nombre" %genre
    nodes = session.run(q1)
    nodes = list(nodes)
    
    for node in nodes:
        if node not in genre_recommendations: #Se revisa que no este repetido
            result = re.split("[']",str(node)) #Se separa por apostrofe
            genre_recommendations.append(result[1]) #La posicion 1 contiene el nombre del artista
            
    return genre_recommendations #Se regresa la lista actualizada
    

aux = get_node_name('Artista')
aux2 = get_node_name('Cancion')
search_node('Lorde')

print(song_recommendation_genre('Dance pop', 'Pop', 'Electro Pop'))
