import re
import random
from Clases import *
from GrafoInicial import *


def realizar_base():
    base = [] #array de array
    final = []
    actual = [] #Llevara los items de cada artista
    
    with open("Base_de_Datos.txt") as f:
        temporal = f.read()
    f.close()
    
    temp = temporal.split('\n')
    temp2 = []
    for i in range(int(len(temp))): 
        temp2.append(temp[i].split(';')) #Se separa por ;

    for item in temp2: #Por elemento en temporal2
        base.append(item) #Se agrega a la base
   
    for artist in base: #Por cada artista en la base
        actual = []
        contador = 1;  #Se tienen tres elementos> nombre, canciones, similares
        if len(artist)==3:
            if contador == 1:
                actual.append(artist[0]) #Se agrega nombre
                contador = contador+1
            if contador == 2:
                temp = []
                result = re.findall("\[(.*?)\]", artist[1])
                
                for item in result:
                    temp2 = item.split(',')
                    temp.append(Cancion(temp2[0], temp2[1], temp2[2])) #Se agregan las canciones
                actual.append(temp)
                contador+=1
            if contador==3:
                result = re.findall("\[(.*?)\]", artist[2])
                for item in result:
                    result = item.split(',')
                actual.append(result) #Se agregan los similares
                final.append(Artista(actual[0], actual[1], actual[2])) #Se inserta el artista actual a la db final
    
    
    return final #Se retorna la base

def mostrar_base():
    final = realizar_base()
    
    info_final = []
    for artista in final: #Por cada artista en la base final
        info_final.append(artista.getInfo()) #Se obtiene su informacion
    
    return info_final #Se retorna

def buscar_artista(nombre_artista):
    final = realizar_base()
    
    for artista in final:
        if(artista.artist_name == nombre_artista):
            return generar_grafo(nombre_artista)
    

def buscar_cancion(grafo):
    final = realizar_base()
    
    seguir = True
    contador = 1 #Empezamos del mas alejado al artista acual
    while(seguir): #Se verifica que este en la base de datos
        posible = grafo[len(grafo)-contador] #Se usa la lista de posibles artistas (posicion del grafo)
        
        for artist in final:
            if artist.artist_name == posible:
                posible = artist.similar_artists #Lista de posibles artistas (similares al posible artista del grafo)
                elegido = random.randint(0, len(posible)-1) #Se genera un numero aleatorio entre los artistas posibles
                artista_actual = posible[elegido] #Se selecciona ese artista
                seguir = False #Ya no hay necesidad de seguir moviendonos
        contador+=1
                    
    for item in final:
        if artista_actual == item.artist_name:
            elegido = random.randint(0, len(item.songs)-1) #Se genera un numero aleatorio entre las canciones posibles
                    
            return item.songs[elegido].getInfo() #Se obtiene una cancion aleatoria
            