# Autores:
# Martin Amado 19020
# Andrea Amaya 19357
# Brandon Hernández 19376
# Laura Tamath 19365
# Fecha: 24/05/2020
# Nombre: driver.py

#Importando las funciones de la base de datos
from database import *
from DB import *

#Para los try
opcionn = True
ejecucion = True
validador = True
validador1 = True
agrega1V = True
agrega2V = True
agrega3V = True
yearV = True

while ejecucion:
    if validador:
        print ('-----------Bienvenido al sistemas de recomendación de música-----------')
        print ('\t1.Buscar por géneros similares \n\t2.Buscar por año similar\n\t3.Buscar lo mejor de ambas décadas')
        print ('\t4.Agregar información\n\t5.Borrar información\n\t6.Salir')

        while opcionn:
            opcion = input('\tIngrese la opción a ejecutar: ')
            print ('\n')
            try:
                opcion = int(opcion)
                opcionn = False

            except ValueError:
                print('Opcion inválida!')
                
    opcionn = True
    
    #Buscar por género similar, pregunta 3 géneros
    if opcion == 1:
        validador1 = True
        while validador1:
            print("Se le mostrará los géneros existentes")
            print(get_node_name('Genero'))
            genero1 = input("Ingrese su primer género favortio: ")
            a = genero1.title()
            genero2 = input("Ingrese su primer género favortio: ")
            b = genero2.title()
            genero3 = input("Ingrese su primer género favortio: ")
            c = genero3.title()
            
            if (search_node(a) and search_node(b) and search_node(c)):
                
                print('Por su inclinación a estos géneros, se recomienda: %s\n' %song_recommendation_genre(a, b, c))
                validador1 = False    
            
        

    #Buscar por año similar, pregunta el año
    if opcion == 2:
        while yearV:
            yearP = input ('¿Música de qué año prefieres escuchar? (2000-2020): ')
            try:
                yearSP = int(yearP)
                if(2000 <= yearSP <= 2020):   
                    print(song_recommendation_year(yearP))
                    yearV = False
                else:
                    print('El año ingresado no está dentro del rango, intentélo de nuevo.')
            except ValueError:
                print('Asegúrese de ingresar enteros')
                
           
         
    #Buscar lo mejor de ambas decadas, no sé que preguntarle gg
    if opcion == 3:
        print('f')#Solo es mientras tanto
         #print(song_recommendation_century()) #Buscando por lo mejor del 2000 B)
        
    #Agregar
    if opcion ==4:
        q1 = "MATCH (x) return (x)"
        nodes = session.run(q1)
        nodes = list(nodes)
        arti = input('Ingrese el nombre del Artista que desea agregar: ')
        ar = arti.capitalize()
        can1 = input('Ingrese una canción de este/a: ')
        ca1 = can1.capitalize()
        gen1 = input ("Ingrese el género de esta: ")
        ge1 = gen1.capitalize()
        while agrega1V :
            year1 = input ('¿En qué año fue lanzada? ')
            try:
                yearr1 = int(year1)
                if (2000 <= yearr1 <=2020):
                    agrega1V = False
                else:
                    print('El año ingresado no se encuentra dentro del rango')
            except ValueError:
                print('Asegurese de ingresar enteros')
        can2 = input('Ingrese otra canción de este/a: ')
        ca2 = can2.capitalize()
        gen2 = input ("Ingrese el género de esta: ")
        ge2 = gen2.capitalize()
        while agrega2V:
            year2 = input ('¿En qué año fue lanzada? ')
            try:
                yearr2 = int(year2)
                if (2000 <= yearr2 <=2020):
                    agrega2V = False
                else:
                    print('El año ingresado no se encuentra dentro del rango')
            except ValueError:
                print('Asegurese de ingresar enteros')
        can3 = input('Ingrese otra canción de este/a: ')
        ca3 = can3.capitalize()
        gen3 = input ("Ingrese el género de esta: ")
        ge3 = gen3.capitalize()
        while agrega3V:
            year3 = input ('¿En qué año fue lanzada? ')
            try:
                yearr3 = int(year3)
                if (2000 <= yearr3 <=2020):
                    agrega3V = False
                else:
                    print('El año ingresado no se encuentra dentro del rango')
            except ValueError:
                print('Asegurese de ingresar enteros')
       
        print(ar, ca1, ca2, ca3, ge1, ge2, ge3, year1, year2, year3)

        DB.agregarDatos(ar, ca1, ca2, ca3, ge1, ge2, ge3, yearr1, yearr2, yearr3)
        for node in nodes:
            print(node)
    
    #Borrar
    if opcion ==5:
        print('f')#Solo es mientras tanto
         
    #Salir
    if opcion == 6:
        print('Gracias por utilizar este sistema de recomendación')
        ejecucion = False