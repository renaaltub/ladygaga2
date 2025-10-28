from funciones import *
from playlist import *


def normalizacion_temas(playlist: dict):
    for i in range(len(playlist)):
        tema = obtener_nombre_tema(playlist[i]["Tema"])
        playlist[i]["Tema"] = tema
        #print(playlist[i]["Tema"])
    return playlist
        

def lista_colaboradores(playlist: dict):
    for i in range(len(playlist)):
        colaboradores = obtener_colaboradores(playlist[i]["Tema"])
        playlist[i]["Colaboradores"] = colaboradores
        #print(playlist[i]["Tema"] )
    return playlist
        
    
def vistas_enteros(playlist: dict):
    for i in range(len(playlist)):
        vistas = convertir_vistas_numerico(playlist[i]["Vistas"])
        playlist[i]["Vistas"] = vistas
#        print(playlist[i]["Vistas"])
    return playlist

def duracion_enteros(playlist: dict):
    for i in range(len(playlist)):
        duracion = convertir_duracion_numerico(playlist[i]["Duracion"])
        playlist[i]["Duracion"] = duracion
#        print(playlist[i]["Duracion"] )
    return playlist

def mostrar_cancion_duracion(playlist: dict):
    for i in range(len(playlist)):
        duracion = convertir_duracion_numerico(playlist[i]["Duracion"])
        playlist[i]["Duracion"] = duracion
#        print(playlist[i]["Duracion"] )
    return playlist

def fecha_normalizacion(playlist: list) -> list:
    for i in range(len(playlist)):
        fecha = formatear_fecha(playlist[i]["Fecha lanzamiento"])
        playlist[i]["Fecha lanzamiento"] = fecha
    return playlist

def normalizar_datos_completos(playlist: list) -> list:
    playlist = normalizacion_temas(playlist)
    playlist = lista_colaboradores(playlist) 
    playlist = vistas_enteros(playlist)
    playlist = duracion_enteros(playlist)
    playlist = fecha_normalizacion(playlist)
    return playlist