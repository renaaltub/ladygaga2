import datetime

def obtener_colaboradores(titulo:str) -> list:
    lista = []
    if buscar_elemento(titulo,"-") == True:
        primer_slicing = separar_elementos(titulo, "-")
        if buscar_elemento(primer_slicing,"|"):
            segundo_slicing = separar_elementos(primer_slicing, "|")
            tercer_slicing = separar_elementos(primer_slicing, "|", False)
            lista.append(segundo_slicing)
            lista.append(tercer_slicing)
        else:
            lista.append(primer_slicing)
    return lista

def separar_elementos(cadena:str, corte:str, valor = True) -> str:
    for i in range(len(cadena)):
        if cadena[i] == corte:
            if valor == True:
                    cadena_modificada = cadena[0:i]
            elif valor == False:
                    cadena_modificada = cadena[i + 1:len(cadena)]
    return cadena_modificada

def buscar_elemento(cadena:str, elemento:str) -> bool:
    resultado = False
    for i in range(len(cadena)):
        if cadena[i] == elemento:
            resultado = True
    return resultado

def obtener_nombre_tema(titulo:str) -> str:
    if buscar_elemento(titulo,"-") == True:
        tema = separar_elementos(titulo, "-", False)
    elif buscar_elemento(titulo,"-") == False:
        tema = titulo
    return tema

def verificar_numero_entero(cadena:str) -> bool:
    resultado = False
    for i in range(len(cadena)):
        if ord(cadena[i]) > 47 and ord(cadena[i]) < 58:
            resultado = True
    return resultado

def convertir_vistas_numerico(vistas:str) -> int:
    separar_enteros = separar_elementos(vistas, " ")
    if verificar_numero_entero(vistas) == True:
        numero = int(separar_enteros)
        separar_palabra = separar_elementos(vistas, " ", False)
        if separar_palabra == "millones" or separar_palabra == "Millones":
            numero *= 1000000
    else:
        numero = None
    return numero

def convertir_duracion_numerico(duracion: str) -> int:
    resultado = None
    if buscar_elemento(duracion, ":") == True:
        separar_minutos = separar_elementos(duracion, ":")
        separar_segundos = separar_elementos(duracion, ":",False)
        if verificar_numero_entero(separar_minutos) and verificar_numero_entero(separar_segundos):
            minutos = int(separar_minutos)
            segundos = int(separar_segundos)
            resultado = (minutos * 60) + segundos
    return resultado

def obtener_codigo(url:str) -> str:
    if buscar_elemento(url, "="):
        codigo = separar_elementos(url, "=", False)
    return codigo

def formatear_fecha(fecha:str) -> datetime:
    resultado = None
    if buscar_elemento(fecha, "-"):
        separar_año_mes = separar_elementos(fecha, "-")
        separar_año = separar_elementos(separar_año_mes, "-")
        separar_mes = separar_elementos(separar_año_mes, "-", False)
        separar_dia = separar_elementos(fecha, "-", False)
        if verificar_numero_entero(separar_año) and verificar_numero_entero(separar_mes) and verificar_numero_entero(separar_dia):
            año = int(separar_año)
            mes = int(separar_mes)
            dia = int(separar_dia)
            resultado = datetime.date(año, mes, dia)
    return resultado

