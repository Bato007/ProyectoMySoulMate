from neo4j import GraphDatabase

db = GraphDatabase.driver("bolt://localhost:7687", auth = ("neo4j", "1234"), encrypted = False)

session = db.session()

def agregarDatos(nombre_artista, cancion_1, cancion_2, cancion_3, genero_1, genero_2, genero_3, year_1, year_2, year_3):
    
    #Se reemplazan espacios con guiones bajos
    nombre2 = nombre_artista.replace(" ", "_")
    cancion1 = cancion_1.replace(" ", "_")
    cancion2 = cancion_2.replace(" ", "_")
    cancion3 = cancion_3.replace(" ", "_")
    genero1 = genero_1.replace(" ", "_")
    genero2 = genero_2.replace(" ", "_")
    genero3 = genero_3.replace(" ", "_")
    
    
    #Se crean el nodo artista, los nodos canciones, y su relacion
    Create_1 = """CREATE(%s:Artista {nombre:"%s"})
    CREATE (%s:Cancion {nombre: "%s"})
    CREATE (%s)-[:PERFORMS]->(%s)
    CREATE (%s:Cancion {nombre: "%s"})
    CREATE (%s)-[:PERFORMS]->(%s)
    CREATE (%s:Cancion {nombre: "%s"})
    CREATE (%s)-[:PERFORMS]->(%s)



    """%(nombre2, nombre_artista, cancion1, cancion_1, nombre2, cancion1, cancion2, cancion_2, nombre2, cancion2, cancion3, cancion_3, nombre2, cancion3)

#Relacion de artista con los diferentes generos
    Genre_1="""MATCH (a:Artista), (b:Genero)
    WHERE a.nombre = '%s' AND b.name = '%s'
    CREATE (a)-[:WRITES]->(b)

    """%(nombre_artista, genero_1)
    
    Genre_2="""MATCH (a:Artista), (b:Genero)
    WHERE a.nombre = '%s' AND b.name = '%s'
    CREATE (a)-[:WRITES]->(b)

    """%(nombre_artista, genero_2)
    
    Genre_3="""MATCH (a:Artista), (b:Genero)
    WHERE a.nombre = '%s' AND b.name = '%s'
    CREATE (a)-[:WRITES]->(b)

    """%(nombre_artista, genero_3)
    
    
    #Relacion de cancion a genero y año
    Song_11="""MATCH (a:Cancion), (b:Genero)
    WHERE a.nombre = "%s" AND b.name = "%s"
    CREATE (a)-[:BELONGS]-> (b)

    """%(cancion_1, genero_1)

    Song_12="""
    MATCH (a:Cancion), (b:Year)
    WHERE a.nombre = "%s" AND b.year = "%s"
    CREATE (a)-[:RELEASED] -> (b)
    """%(cancion_1, year_1)
    
    #Cancion 2
    Song_21="""MATCH (a:Cancion), (b:Genero)
    WHERE a.nombre = "%s" AND b.name = "%s"
    CREATE (a)-[:BELONGS]-> (b)

    """%(cancion_2, genero_2)

    Song_22="""
    MATCH (a:Cancion), (b:Year)
    WHERE a.nombre = "%s" AND b.year = "%s"
    CREATE (a)-[:RELEASED] -> (b)
    """%(cancion_2, year_2)
    
    #Cancion 3
    
    Song_31="""MATCH (a:Cancion), (b:Genero)
    WHERE a.nombre = "%s" AND b.name = "%s"
    CREATE (a)-[:BELONGS]-> (b)

    """%(cancion_3, genero_3)

    Song_32="""
    MATCH (a:Cancion), (b:Year)
    WHERE a.nombre = "%s" AND b.year = "%s"
    CREATE (a)-[:RELEASED] -> (b)
    """%(cancion_3, year_3)
    
    
    session.run(Create_1)
    
    session.run(Genre_1)
    if genero_1 != genero_2:
        session.run(Genre_2)
        
    if genero_3 != genero_1 and genero_3 != genero_2:
        session.run(Genre_3)
        
        
    session.run(Song_11)
    
    session.run(Song_12)
    
    session.run(Song_21)
    
    session.run(Song_22)
    
    session.run(Song_31)
    
    session.run(Song_32)
    
