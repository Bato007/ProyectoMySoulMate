# Autores:
# Martin Amado 19020
# Andrea Amaya 19357
# Brandon Hernández 19376
# 
# Fecha: 6-05-2020
# Nombre: Main.py

# Importando 
import Base_de_Datos as BD

# Variables
opcion = "0"
nombre_artista = ""
grafo = []
recomendaciones = [ ]
aux = ""

# Iniciando Menu

while(opcion != "3"):
    print("|\n|\tBienvenido a su Recomendador de Canciones")
    # Mostrando menu
    print("|\n| 1. Obtener Recomendacion")
    print("| 2. Historial de Recomendaciones")
    print("| 3. Salir")
    opcion = input("| Ingrese lo que desea hacer: ")
    
    if (opcion == "1"):
        print("|\n| Se cuentan con los siguientes artistas:")
        
        # Mostrando Base de Datos
        for i in BD.mostrar_base():
            aux = "| "
            for j in i:
                aux += j
            print(aux)
            
        print("| Como se muestra en la base de datos por favor")
        nombre_artista = input("| Ingrese su artista favorito para recomendarle una cancion: ")
        
        # Consiguiendo al cuate
        grafo = BD.buscar_artista(nombre_artista)
        
        # Verificando que este el artista
        if (grafo != None):
            grafo = BD.buscar_cancion(grafo)
        
            # Mostrando la recomendacion
            aux = "|"
            aux += grafo
            
            # Verificando si hay 3 elementos en recomendaciones
            if (len(recomendaciones) == 3):
                recomendaciones.pop()
            
            recomendaciones.append(aux)
        
        # Si no esta el artista
        else:
            aux = "| El artista ingresado no se encuentra en la lista"
            
        print(aux)
        
    # Mostrar recomendaciones pasadas
    elif(opcion == "2"):
        
        print("|\n| Se han recomendado las siguientes canciones:")
        if (len(recomendaciones) > 0):
            for i in recomendaciones:
                print("%s" %i)
        else:
             print("| No hay recomendaciones")
             
    # Salida y opcion invalida
    elif(opcion == "3"):
        print("| Esperamos le gustaran las recomendaciones")
    else:
        print("| Opcion invalida")
        