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
        print ('\t1.Buscar por géneros similares \n\t2.Buscar por artista similar\n\t3.Buscar lo mejor de ambas décadas')

        while opcionn:
            opcion = input('\tIngrese la opción a ejecutar: ')
            print ('\n')
            try:
                opcion = int(opcion)
                opcionn = False

            except ValueError:
                print('Opcion inválida!')
                
    opcionn = True
    
    #Buscar por artista similar
    if opcion == 1:
         print('v') #Solo es mientras tanto

    #Buscar por artista similar
    if opcion == 2:
         print('f')#Solo es mientras tanto
    #Buscar lo mejor de ambas decadas
    if opcion == 3:
         print('g')#Solo es mientras tanto
    #Salir
    if opcion == 4:
        print('Gracias por utilizar este sistema de recomendación')
        ejecucion = False