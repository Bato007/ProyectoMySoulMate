# Autores:
# Martin Amado 19020
# Andrea Amaya 19357
# Brandon Hernández 19376
# Laura Tamath 19365
# Fecha: 24/05/2020
# última modificación: 27/05/2020
# Nombre: driver.py

#Importando las funciones de la base de datos
from database import *
import DB


recomendaciones = []
#Para los try
opcionn = True
ejecucion = True
validador = True
validador1 = True
agrega1V = True
agrega2V = True
agrega3V = True
yearV = True
delV = True

while ejecucion:
    
    print ('\n-----------Bienvenido al sistemas de recomendación de música-----------')
    print ('\t1. Buscar por géneros similares \n\t2. Buscar por año similar\n\t3. Buscar lo mejor de ambas décadas')
    print ('\t4. Agregar información\n\t5. Borrar información\n\t6. Ver ultimas recomendaciones\n\t7. Salir')
    opcion = input('\tIngrese la opción a ejecutar: ')
    
    if len(recomendaciones) > 3:
        recomendaciones.pop()
    
    #Buscar por género similar, pregunta 3 géneros
    if opcion == '1':
        validador1 = True
        while validador1:
            print("Se le mostrará los géneros existentes")
            print(get_node_name('Genero'))
            genero1 = input("Ingrese su primer género favorito: ")
            a = genero1.title()
            genero2 = input("Ingrese su segundo género favorito: ")
            b = genero2.title()
            genero3 = input("Ingrese su tercer género favorito: ")
            c = genero3.title()
            
            if (search_node(a) and search_node(b) and search_node(c)):
                aux = song_recommendation_genre(a, b, c)
                print('Por su inclinación a estos géneros, se recomienda: %s\n' %aux)
                recomendaciones.append(aux)
                validador1 = False           

    #Buscar por año similar, pregunta el año
    elif opcion == '2':
        while yearV:
            yearP = input ('¿De qué año prefieres escuchar música? (2000-2020): ')
            try:
                yearSP = int(yearP)
                if(2000 <= yearSP <= 2020):
                    aux = song_recommendation_year(yearP)
                    print('Se recomienda: ', aux)
                    recomendaciones.append(aux)
                    yearV = False
                else:
                    print('El año ingresado no está dentro del rango, intentélo de nuevo.')
            except ValueError:
                print('Asegúrese de ingresar enteros')
                    
    #Buscar lo mejor de ambas decadas, no sé que preguntarle gg
    elif opcion == '3':
        aux = song_recommendation_century()
        print('Lo mejor de este siglo fue: ', aux)
        recomendaciones.append(aux)
        
    #Agregar
    elif opcion == '4':
        arti = input('Ingrese el nombre del Artista que desea agregar: ')
        ar = arti.title()
        can1 = input('Ingrese una canción de este/a: ')
        ca1 = can1.capitalize()
        gen1 = input ("Ingrese el género de esta: ")
        ge1 = gen1.title()
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
        ge2 = gen2.title()
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
        ge3 = gen3.title()
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
       

        DB.agregarDatos(ar, ca1, ca2, ca3, ge1, ge2, ge3, yearr1, yearr2, yearr3)
        print('Se agregó con éxito.')
    
    #Borrar
    elif opcion == '5':
        delV = True
        while delV:
            arti = input('Ingrese el nombre del Artista/Cancion que desea eliminar: ')
            ar = arti.title()
            if (search_node(ar)):
                flag = delete_node(ar)
                if flag == True:
                    print('Se ha eliminado con éxito')
                else:
                    print('El artista no se puede eliminar de la base de datos')
                delV = False
            else: 
                print('No se puede eliminar, pues este no existe')
    
    # Recomendaciones
    elif opcion == '6':
        print('\nLas ultimas recomendaciones fueron:')
        for i in recomendaciones:
            print(i)
        
    #Salir
    elif opcion == '7':
        print('Gracias por utilizar este sistema de recomendación')
        ejecucion = False
    
    else:
        print('Ingrese una opcion valida')