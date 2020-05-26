# Autores:
# Martin Amado 19020
# Andrea Amaya 19357
# Brandon Hernández 19376
# Laura Tamath 19365
# Fecha: 24/05/2020
# Nombre: driver.py

#Importando las funciones de la base de datos
#import database as *

opcionn = True
ejecucion = True
validador = True

while ejecucion:
    if validador:
        print ('-----------Bienvenido al sistemas de recomendación de música-----------')
        print ('\t1.Buscar por géneros similares \n\t2.Buscar por año similar\n\t3.Buscar lo mejor de ambas décadas\n\t4.Salir')

        while opcionn:
            opcion = input('\tIngrese la opción a ejecutar: ')
            print ('\n')
            try:
                opcion = int(opcion)
                opcionn = False

            except ValueError:
                print('Opcion inválida!')
                
    opcionn = True
    
    #Buscar por género similar
    if opcion == 1:
        print('f')#Solo es mientras tanto
        #print(get_node_name('Artista')) #Muestra los generos posibles
        #print(song_recommendation_genre('Dance pop', 'Pop', 'Electro Pop')) #Buscando por generos similares
        #print(song_recommendation_year('2010')) #Buscando por año similar
        

    #Buscar por año similar
    if opcion == 2:
         print('f')#Solo es mientras tanto
         
    #Buscar lo mejor de ambas decadas
    if opcion == 3:
        print('f')#Solo es mientras tanto
         #print(song_recommendation_century()) #Buscando por lo mejor del 2000 B)
         
    #Salir
    if opcion == 4:
        print('Gracias por utilizar este sistema de recomendación')
        ejecucion = False