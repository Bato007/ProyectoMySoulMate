# Autores:
# Martin Amado 19020
# Andrea Amaya 19357
# Brandon Hernández 19376
# 
# Fecha: 6-05-2020
# Nombre: Clases.py

class Artista:
    
    # Constructor de un artista
    # Param: Nombre del artista, la lista de canciones y artistas similares
    def __init__(self, artist_name, songs, similar_artists):
        self.artist_name = artist_name
        self.songs = songs[:]
        self.similar_artists = similar_artists[:]
    
    # Deuelve la informacion del autor
    # return: string con el nombre, numero de canciones y numero de artistas similares
    def getInfo(self):
        return self.artist_name, "tiene", len(self.songs), "canciones en la base de datos y", len(self.similar_artists), "artistas similares"
            
class Cancion:
    
    # Constructor de la cancion
    # Param: Nombre de la cancion, nombre del album y genero
    def __init__(self, song_name, album, song_genre):
        self.song_name = song_name
        self.album = album
        self.song_genre = song_genre
    
    # Deuelve la informacion de la cancion
    # return: string con el nombre, numero del album y el genero
    def getInfo(self):    
        return "La cancion", self.song_name,"pertenece al album",self.album,"del genero",self.song_genre