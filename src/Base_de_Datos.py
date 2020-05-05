import re
from Clases import *

def realizar_base():
    base = [] #array de array
    actual = [] #Llevara los items de cada artista
    final = [] #La base final a retornar
    
    with open("Base_de_Datos.txt") as f:
        temporal = f.read()
    f.close()
    
    temp = temporal.split('\n')
    temp2 = []
    for i in range(int(len(temp)/2)): #Se agarra la mitad para no agregar los array de enters
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
