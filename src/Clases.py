class Artista:
    
    def __init__(self, artist_name, songs, similar_artists):
        self.artist_name = artist_name
        self.songs = songs[:]
        self.similar_artists = similar_artists[:]
    
    def getInfo():
        return self.artist_name, "tiene",self.songs.len(), "canciones en la base de datos y", self.similar_artist.len(), "artistas similares"
            
class Cancion:
    
    def __init__(self, song_name, album, song_genre):
        self.song_name = song_name
        self.album = album
        self.song_genre = song_genre
        
    def getInfo():    
        return "La cancion", self.song_name,"pertenece al album",self.album,"del genero",self.song_genre