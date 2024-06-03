from queue import Queue as Cola
from random import randint
#EJ 13
def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Cola[int]:
    c:Cola[int] = Cola()
    for i in range (cantidad):
        c.put(randint(desde, hasta))
    return c

def imprimir_cola(cola:Cola[int]):
    lista_aux:list[int] = []
    while not cola.empty():
        lista_aux.append(cola.get())

    print(lista_aux)

    for i in range(len(lista_aux)):
        cola.put(lista_aux)

#EJ 19
def contar_apariciones(i:int, longitudes:list[int]) -> int:
    aparece:int = 0
    for j in longitudes:
        if j == i:
            aparece += 1
    return aparece

"""
def agrupar_por_longitud(nombre_archivo:str) -> dict[int,int]:
    f = open(nombre_archivo)
    contenido = f.readlines()
    f.close

    d:dict[int,int] = {}
    i:int = 0
    cuento_letras:int = 0
    longitudes:list[int] = []
    for linea in contenido:
        for i in range(0, len(linea), 1):
            if (i == len(linea)-1):
                longitudes.append(cuento_letras)
                cuento_letras = 0

            if (linea[i] == " "):
                longitudes.append(cuento_letras)
                cuento_letras = 0
            else:
                cuento_letras += 1
    for i in longitudes:
        d[i] = contar_apariciones(i, longitudes)
    return d
"""

"""
def agrupar_por_longitud(nombre_archivo:str) -> dict[int, int]:
    f = open(nombre_archivo)
    contenido = f.readlines()
    f.close
    longitudes:dict[int,int] = {}

    for linea in contenido:
        for palabra in linea.split():
            if len(palabra) in longitudes.keys():
                longitudes[len(palabra)] += 1
            else:
                longitudes[len(palabra)] = 1

    return longitudes
print(agrupar_por_longitud("longitud_palabras.txt"))
"""

def la_palabra_mas_frecuente(nombre_archivo:str) -> str:
    f = open(nombre_archivo)
    contenido = f.readlines()
    f.close

    apariciones:dict[str:int] = {}
    palabra_mas_frecuente:str = ""
    for linea in contenido:
        for palabra in linea.split():
            if palabra in apariciones.keys():
                apariciones[palabra] += 1
                palabra_mas_frecuente = palabra
            else:
                apariciones[palabra] = 1
        for palabra in apariciones.keys():
            if apariciones[palabra_mas_frecuente] < apariciones[palabra]:
                palabra_mas_frecuente = palabra
    
    return palabra_mas_frecuente
#print(la_palabra_mas_frecuente("longitud_palabras.txt"))