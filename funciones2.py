from funciones import *
from normalizacion import *
import datetime

def lista_temas(playlist: dict):
    temas = []
    for i in range(len(playlist)):
        temas.append(playlist[i]["Tema"])     
    return temas


def ordenar_por_duracion(playlist: list) -> list:
    for i in range(len(playlist)):
        for j in range(0, len(playlist)-i-1):
            if playlist[j]["Duracion"] < playlist[j+1]["Duracion"]:
                playlist[j], playlist[j+1] = playlist[j+1], playlist[j]
    return playlist


def lista_de_colaboradores(playlist: dict):
    colaboradores = []
    for i in range(len(playlist)):
        colaboradores.append(playlist[i]["Colaboradores"])     
    return colaboradores