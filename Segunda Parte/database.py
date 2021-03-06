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

# Se abre la sesion de Neo4j
db = GraphDatabase.driver("bolt://localhost:7687",
                          auth =("neo4j","1234"), encrypted = False)
session = db.session()


# Obtiene los nombres de todos los Generos
# pre: La base de datos debe de tener al menos un dato,
#      debe de ser un 'Genero', 'Artista' o 'Cancion
# Param: El nombre del label del nodo
# Return: Una lista con todos los nombres de artistas que hay en la base de datos
def get_node_name(node_type):
    temp = [] # Guarda los nombres de los artistas
    q1 = "MATCH (x:%s) RETURN x" %node_type
    nodes = session.run(q1)
    nodes = list(nodes)
 
    # Metiendo los nombres al 
    try:
        for node in nodes:
            temp.append(dict(dict(node)['x'])['name'])
    except:
        for node in nodes:
            temp.append(dict(dict(node)['x'])['nombre'])
    return temp

# Busca el nodo que quiere el usuario 
# pre: La base de datos debe de tener al menos un dato,
#      debe de ser una 'Cancion' o un 'Artista'
# Param: El nombre del artista/cancion
# Return: True si se encontro al artista, False si no se encontro
def search_node(searched_node):
    temp = [] # Guarda los nombres de los artistas
    q1 = "MATCH (x:Artista) RETURN x" 
    nodes = session.run(q1)
    nodes = list(nodes)
 
    # Metiendo los nombres al 
    for node in nodes:
        temp.append(dict(dict(node)['x'])['nombre'])
        
    q1 = "MATCH (x:Cancion) RETURN x" 
    nodes = session.run(q1)
    nodes = list(nodes)
 
    # Metiendo los nombres al 
    for node in nodes:
        temp.append(dict(dict(node)['x'])['nombre'])
        
    q1 = "MATCH (x:Genero) RETURN x" 
    nodes = session.run(q1)
    nodes = list(nodes)
 
    # Metiendo los nombres al 
    for node in nodes:
        temp.append(dict(dict(node)['x'])['name'])
        
    q1 = "MATCH (x:Year) RETURN x" 
    nodes = session.run(q1)
    nodes = list(nodes)
 
    # Metiendo los nombres al 
    for node in nodes:
        temp.append(dict(dict(node)['x'])['year'])
        
    if (searched_node in temp):
        return True
    else:
        return False

# Borra el nodo que el usuario quiere
# pre: La base de datos debe de tener al menos un dato,
#      debe de ser una 'Cancion' o un 'Artista'
#      Se debe de verificar que el artista a eliminar este en
#      la base de datos
# pos: hay n - 1 en la base de datos
# Param: El nombre del artista/cancion
# Return: True si se pudo borrar el artista o False si no se pudo
def delete_node(delete_node):
    aux = []
    temp = []
    
    # Consiguiendo las cancinoes que no se pueden borrar
    q = "MATCH (x)-[:SOTY]->(y) RETURN y.nombre"
    nodes = session.run(q)
    aux = list(nodes)
    for node in aux:
        temp.append(dict(node)['y.nombre'])
    
    # Consiguiendo los artistas que no se pueden borrar
    q = "MATCH (x)-[r:AOTY]->(y) RETURN y.nombre"
    nodes = session.run(q)
    aux = list(nodes)
    for node in aux:
        temp.append(dict(node)['y.nombre'])
    
    # Consiguiendo los generos, porque no se pueden borrar
    q1 = "MATCH (x:Genero) RETURN x" 
    nodes = session.run(q1)
    nodes = list(nodes)
    for node in nodes:
        temp.append(dict(dict(node)['x'])['name'])
        
    # Metiendo los años, ya que no se pueden borrar
    q1 = "MATCH (x:Year) RETURN x" 
    nodes = session.run(q1)
    nodes = list(nodes)
    for node in nodes:
        temp.append(dict(dict(node)['x'])['year'])
         
    # Verificando que no este entre los que no se pueden borrar
    if (delete_node in temp):
        return False
    else: # Al no estar en las listas, procede a borrar
        q = "MATCH (x {nombre:'%s'}) DETACH DELETE x" %delete_node
        nodes = session.run(q)
        return True

#Params-> generos que le gustan
#Return-> cancion aleatoria
def song_recommendation_genre(genre1, genre2, genre3):
    genre_recommendations = []
    genre_recommendations = doing_genre_rec(genre1, genre_recommendations) #Realizando recomendacion genero 1
    genre_recommendations = doing_genre_rec(genre2, genre_recommendations) #Realizando recomendacion genero 2
    genre_recommendations = doing_genre_rec(genre3, genre_recommendations) #Realizando recomendacion genero 3
    
    random_song = random.randrange(len(genre_recommendations)) #Generando artista al azar
    song = genre_recommendations[random_song] #Eligiendo artista

    #Retornando cancion - artista
    return song

#Params-> genero, lista de artistas generados por genero
#Return-> lista de artistas generados por genero
def doing_genre_rec(genre, genre_recommendations):
    #Buscando en la base por genero
    q1 = "MATCH (n)-[:PERFORMS]-(cancion:Cancion)-[:BELONGS]-(Genero{name: '%s'}) return n.nombre, cancion.nombre" %genre
    nodes = session.run(q1)
    nodes = list(nodes)
    
    
    for node in nodes:
        if node not in genre_recommendations: #Se revisa que no este repetido
            result = re.split("[']",str(node)) #Se separa por apostrofe
            
            if(len(result)!=5): #Significa que la cancion tiene apostrofe
                artist = result[1] #Entonces, el artista es posicion 1
                result = re.split('["]',str(node)) #Se separa por comillas
                genre_recommendations.append(artist + " - " + result[1]) #La posicion 1 contiene el nombre de la cancion 
            else:
                genre_recommendations.append(result[1]+ " - " + result[3]) #La posicion 1 contiene el nombre del artista, la posicion 3 el nombre de la cancion 
            
            
    return genre_recommendations #Se regresa la lista actualizada

#Params-> año a buscar
#Return-> cancion aleatoria
def song_recommendation_year(year):
    year_recommendations = []
    
    #Se recomiendan de un año antes, el año elegido y un año después
    year_recommendations = doing_year_rec(str(int(year)-1), year_recommendations)
    year_recommendations = doing_year_rec(year, year_recommendations)
    year_recommendations = doing_year_rec(str(int(year)+1), year_recommendations)
    
    #Generando cancion aleatoria
    random_song = random.randrange(len(year_recommendations))
    
    return year_recommendations[random_song]

#Params-> año, lista de artistas generados por año
#Return-> lista de artistas generados por año
def doing_year_rec(year, year_recommendations):
    #Buscando en la base por año 
    q1 = "MATCH (artista:Artista) -[:PERFORMS]-(cancion:Cancion)-[:RELEASED]-(Year{year:'%s'}) return cancion.nombre, artista.nombre" %year
    nodes = session.run(q1)
    nodes = list(nodes)
    
    for node in nodes:
        if node not in year_recommendations: #Se revisa que no este repetido
            result = re.split("[']",str(node)) #Se separa por apostrofe
            
            if(len(result)!=5): #Significa que la cancion tiene apostrofe
                artist = result[2] #Entonces, el artista es posicion 2
                result = re.split('["]',str(node)) #Se separa por comillas
                year_recommendations.append(result[1]+ " - " + artist) #La posicion 1 contiene el nombre de la cancion 
            else:
                year_recommendations.append(result[1]+ " - " + result[3]) #La posicion 1 contiene el nombre del artista, la posicion 3 el nombre de la cancion 
            
            
          
    return year_recommendations #Se regresa la lista actualizada

#Params-> ninguno
#Return-> cancion aleatoria del siglo
def song_recommendation_century():
    century_recommendations = []
    century_recommendations = doing_century_rec(century_recommendations)
    
    #Generando cancion aleatoria
    random_song = random.randrange(len(century_recommendations))
    
    return century_recommendations[random_song]

#Params-> lista de artistas generados por siglo
#Return-> lista de artistas generados por siglo
def doing_century_rec(century_recommendations):
    #Buscando en la base por cancion del año
    q1 = "MATCH (year:Year)-[:SOTY]-(cancion:Cancion)-[:PERFORMS]-(artist:Artista) return cancion.nombre, artist.nombre"
    nodes = session.run(q1)
    nodes = list(nodes)
    
    for node in nodes:
        if node not in century_recommendations: #Se revisa que no este repetido
            result = re.split("[']",str(node)) #Se separa por apostrofe
            
            if(len(result)!=5): #Significa que la cancion tiene apostrofe
                artist = result[2] #Entonces, el artista es posicion 2
                result = re.split('["]',str(node)) #Se separa por comillas
                century_recommendations.append(result[1]+" - " + artist) #La posicion 1 contiene el nombre de la cancion 
            else:
                century_recommendations.append(result[1]+ " - " + result[3]) #La posicion 1 contiene el nombre del artista, la posicion 3 el nombre de la cancion 
            
    #Buscando en la base por artista del año
    q1 = "MATCH (year:Year)-[:AOTY]-(artist:Artista)-[:PERFORMS]-(cancion:Cancion) return cancion.nombre, artist.nombre"
    nodes = session.run(q1)
    nodes = list(nodes)
    
    for node in nodes:
        if node not in century_recommendations: #Se revisa que no este repetido
            result = re.split("[']",str(node)) #Se separa por apostrofe
            
            if(len(result)!=5): #Significa que la cancion tiene apostrofe
                artist = result[2] #Entonces, el artista es posicion 2
                result = re.split('["]',str(node)) #Se separa por comillas
                century_recommendations.append(result[1]+" - " + artist) #La posicion 1 contiene el nombre de la cancion 
            else:
                century_recommendations.append(result[1]+ " - " + result[3]) #La posicion 1 contiene el nombre del artista, la posicion 3 el nombre de la cancion 
            
    return century_recommendations #Se regresa la lista actualizada
