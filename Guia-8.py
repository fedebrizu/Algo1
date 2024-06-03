#EJ 1.1
def contar_lineas(nombre_archivo:str) -> int:
    res:int = 0
    f = open(nombre_archivo)
    res = len(f.readlines())
    f.close()
    return res
#print(contar_lineas("Guia-8.txt"))

#EJ 1.2
def existe_palabra(palabra:str, nombre_archivo:str) -> bool:
    res:bool = False
    f = open(nombre_archivo)
    contenido:list[str] = f.readlines()
    for linea in contenido:
        if palabra in linea:
            res = True
    f.close()
    return res

#EJ 1.3
def cantidad_apariciones(palabra:str, nombre_archivo:str) -> int:
    res:int = 0
    f = open(nombre_archivo)
    if existe_palabra(palabra, nombre_archivo):
        for linea in f.readlines():
            if palabra in linea:
                res += cantidad_apariciones_aux(palabra, linea)
    else:
        res = 0
    f.close()
    return res

def cantidad_apariciones_aux(palabra:str, linea:str) -> int:
    res:int = 0
    i:int = 0
    coincidencias:int = 0
    while i < (len(linea) - 1):
        if linea[i] == palabra[0]:
            for j in range (0, len(palabra), 1):
                if linea[i] == palabra[j]:
                    i += 1
                    coincidencias += 1
                else:
                    j = len(palabra)
            if coincidencias == len(palabra):
                res += 1
                i -= 1
            coincidencias = 0
        i += 1
    return res
#print(cantidad_apariciones("esto", "Guia-8.txt"))

#EJ 2
def clonar_sin_comentarios(nombre_archivo:str):
    f_original = open(nombre_archivo)
    salida:list[str] = []
    for linea in f_original.readlines():
        if not es_un_comentario(linea):
            salida.append(linea)
    f_original.close()
    nombre_sin_comentarios:str = "Guia-8_sin_comentar.txt"

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
#clonar_sin_comentarios("Guia-8.txt")


#EJ 3
def invertir_lineas(nombre_archivo:str):
    f_original = open(nombre_archivo)
    contenido = f_original.readlines()
    f_original.close()
    
    reverso:list[str] = []
    for i in range (0,len(contenido), 1):
        reverso.append(contenido[len(contenido) - 1 - i]) 

    f_reverso = open("Guia-8_reverso.txt", "w")
    f_reverso.writelines(reverso)
    f_reverso.close()
    return
#invertir_lineas("Guia-8.txt")

#EJ 4
def agregar_frase_al_final(nombre_archivo:str, frase:str):
    f = open(nombre_archivo, "r")
    contenido:str = f.readlines()
    f.close()

    contenido.append(frase)

    f = open(nombre_archivo, "w")
    f.writelines(contenido)
    f.close()
    return
#agregar_frase_al_final("Guia-8.txt", " frase al final")

#EJ 5
def agregar_frase_al_principio(nombre_archivo:str, frase:str):
    f = open(nombre_archivo, "r")
    contenido:str = f.readlines()
    f.close()

    contenido.append(frase)
    for i in range(0, len(contenido), 1):
        contenido[len(contenido) - 1 - i] = contenido[len(contenido) - 2 - i]
        if i == len(contenido) - 1:
            contenido[0] = frase
    f = open(nombre_archivo, "w")
    f.writelines(contenido)
    f.close()
    return
#agregar_frase_al_principio("Guia-8.txt", "frase al principio ")

#EJ 6



#EJ 7
def calcular_promedio_por_estudiante(nombre_archivo_notas:str, nombre_archivo_promedios:str):
    f_notas = open(nombre_archivo_notas)
    contenido = f_notas.readlines()
    f_notas.close()

    lista_lu:list[str] = []
    lista_lu = tomar_lu(lista_lu, nombre_archivo_notas)
    promedios:list[str] = []
    
    for i in range (0, len(lista_lu), 1):
        promedios.append(lista_lu[i] + " -> " + str(promedio_estudiante(nombre_archivo_notas, lista_lu[i])) + "\n")

    f_prom = open(nombre_archivo_promedios, "w")
    f_prom.writelines(promedios)
    f_prom.close()
    return

def tomar_lu(lista_lu:list[str], nombre_archivo):
    f = open(nombre_archivo)
    contenido = f.readlines()
    f.close()

    lu:str = "xxx-xx"
    cant_alumnos = 0

    for linea in contenido:
        if not (lu in linea):
            lu = ""
            for c in range(0,6,1): #las lu tienen 6 caracteres
                   lu += linea[c]
            lista_lu.append(str(lu))
    return lista_lu

def promedio_estudiante(nombre_archivo:str, lu:str) -> float:
    f = open(nombre_archivo)
    contenido = f.readlines()
    f.close()

    comas:int = 0
    i:int = 0
    nota_str:str = []
    suma_notas:float = 0
    cant_notas:int = 0
    promedio:float = 0

    for linea in contenido:
        if lu in linea:
            while comas < 3:
                if linea[i] == ",":
                    comas += 1
                i += 1
            comas = 0
            if (linea[i] == "1"):
                nota_str = "10"
            else:
                nota_str = linea[i]
            i = 0
            suma_notas += float(nota_str)
            cant_notas += 1
    
    promedio = suma_notas / cant_notas
    return promedio
#calcular_promedio_por_estudiante("Guia-8-EJ7-notas.csv", "Guia-8-EJ7-promedios.csv")
