from funciones import *
from playlist import *



    # tema = obtener_nombre_tema(playlist_lady_gaga[0]["Tema"])
    # playlist_lady_gaga[indice]["Tema"] = tema
    # print(playlist_lady_gaga[0]["Tema"] )

def lista_temas(playlist: dict):
    for i in range(len(playlist)):
        tema = obtener_nombre_tema(playlist[i]["Tema"])
        playlist[i]["Tema"] = tema
        print(playlist[i]["Tema"] )
        
        
        
def lista_colaboradores(playlist: dict):
    for i in range(len(playlist)):
        colaboradores = obtener_colaboradores(playlist[i]["Tema"])
        playlist[i]["Colaboradores"] = colaboradores
        print(playlist[i]["Tema"] )