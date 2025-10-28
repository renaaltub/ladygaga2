from funciones import *
from funciones2 import *
from playlist import *
from normalizacion import * 

playlist_normalizada = normalizar_datos_completos(playlist_lady_gaga)

while True:
    opcion = input("1. Mostar lista de temas\n2. Temas ordenados por duracion\n3. Promedio de vistas\n4. Video/s mas visto/s\n5. Video/s menos visto/s\n6. Buscar video por codigo\n7. Listar colaborador\n8. Listar por mes de lanzamiento\n9. Salir\nElija una: ")
    match opcion:
        case "1":
            print(lista_temas(playlist_lady_gaga))
        case "2":
            print(mostrar_cancion_duracion(playlist_lady_gaga))
        case "3":
            pass
        case "4":
            pass
        case "5": 
            pass
        case "6":
            pass
        case "7": 
            print(lista_colaboradores(playlist_lady_gaga))
        case "8": 
            pass
        case "9":
            print("Salir")
            break
