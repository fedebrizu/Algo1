
#Guia 8
#EJ 1
def contar_lineas(nombre_archivo:str) -> int:
    res:int = 0
    f = open(nombre_archivo)
    res = len(f.readlines())
    f.close()
    return res
#print(contar_lineas("ej1.txt"))


"""
def clonar_sin_comentarios(nombre_archivo:str):
    f_original = open(nombre_archivo)
    salida:list[str] = []
    for linea in f_original.readlines():
        if not es_un_comentario(linea):
            salida.append(linea)
    f_original.close()
    nombre_sin_comentarios:str = "sin_comentar_" + nombre_archivo

    f_sin_comentar = open(nombre_sin_comentarios, "w") #para escribir en el txt, por default solo lee. Si no existe el archivo, lo crea
    f_sin_comentar.writelines(salida)
    f_sin_comentar.close()
    return

def es_un_comentario(linea:str) -> bool:
    es_comentario:bool = False
    i:int = 0
    while linea[i] == " ":
        i += 1
    if linea[i] == "#":
        es_comentario = True
    return es_comentario
clonar_sin_comentarios("clase-29-05.py")
"""

def existe_palabra(palabra:str, nombre_archivo:str) -> bool:
    res:bool = False
    f = open(nombre_archivo)
    contenido:list[str] = f.readlines()
    for linea in contenido:
        if pertenece(palabra, linea):
            res = True
    f.close()
    return res

def pertenece(palabra:str, linea:str) -> bool:
    i:int = 0
    while linea[i] != palabra[0] and i < len(linea):
        if i == len(linea) - 1:
            return False
        i += 1
    for letra in palabra:
        if letra == linea[i]:
            i += 1
        else:
            return False
    return True

print(existe_palabra("return", "sin_comentar_clase-29-05.py"))
