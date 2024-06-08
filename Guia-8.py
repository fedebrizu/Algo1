from queue import Queue
from queue import LifoQueue
from random import randint
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
    lista_lu:list[str] = []
    lista_lu = tomar_lu(lista_lu, nombre_archivo_notas)
    promedios:list[str] = []
    
    for i in range (0, len(lista_lu), 1):
        promedios.append(lista_lu[i] + " -> " + str(promedio_estudiante(nombre_archivo_notas, lista_lu[i])) + "\n")

    f_prom = open(nombre_archivo_promedios, "w")
    f_prom.writelines(promedios)
    f_prom.close()
    return

def tomar_lu(lista_lu:list[str], nombre_archivo) -> list[str]:
    f = open(nombre_archivo)
    contenido = f.readlines()
    f.close()

    lu:str = "xxx-xx"

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

#EJ 8
def generar_nros_al_azar_pila(cantidad:int, desde:int, hasta:int) -> LifoQueue[int]:
    pila = LifoQueue()
    for i in range(cantidad):
        pila.put(randint(desde, hasta))
    return pila

def imprimir_pila(pila:LifoQueue[int]):
    lista_aux:list[int] = []
    lista_invertida:list[int] = []
    
    while not pila.empty():
        lista_aux.append(pila.get())
    
    for i in range(0, len(lista_aux), 1):
        lista_invertida.append(lista_aux[len(lista_aux) - 1 - i])
    
    print(lista_invertida)
    
    for num in lista_invertida:
        pila.put(num)

    return
#imprimir_pila(generar_nros_al_azar_pila(5,1,10))

#EJ 9
def cantidad_elementos_pila(p:LifoQueue[int]) -> int:
    lista_aux:list[int] = []
    lista_invertida:list[int] = []
    
    while not p.empty():
        lista_aux.append(p.get())
    
    for i in range(0, len(lista_aux), 1):
        lista_invertida.append(lista_aux[len(lista_aux) - 1 - i])

    for num in lista_invertida:
        p.put(num)
    res:int = len(lista_aux)
    return res
#print(cantidad_elementos_pila(generar_nros_al_azar_pila(8, 1, 10)))

#EJ 10
def buscar_el_maximo_pila(p:LifoQueue[int]) -> int:
    lista_aux:list[int] = []
    lista_invertida:list[int] = []

    while not p.empty():
        lista_aux.append(p.get())
    
    valor_maximo:int = lista_aux[0]
    for i in lista_aux:
        if i > valor_maximo:
            valor_maximo = i

    for i in range(0, len(lista_aux), 1):
        lista_invertida.append(lista_aux[len(lista_aux) - 1 - i])

    for num in lista_invertida:
        p.put(num)

    #imprimir_pila(p)
    return valor_maximo
#print(buscar_el_maximo_pila(generar_nros_al_azar_pila(5, 1, 10)))

#EJ 11


#EJ 12


#EJ 13
def generar_nros_al_azar_cola(cantidad:int, desde:int, hasta:int) -> Queue[int]:
    c:Queue[int] = Queue()
    for i in range (cantidad):
        c.put(randint(desde, hasta))
    return c

def imprimir_cola(cola:Queue[int]):
    lista_aux:list[int] = []
    while not cola.empty():
        lista_aux.append(cola.get())

    print(lista_aux)

    for i in range(len(lista_aux)):
        cola.put(lista_aux[i])
    return
#imprimir_cola(generar_nros_al_azar_cola(5,1,10))

#EJ 14
def cantidad_elementos_cola(c:Queue[int]) -> int:
    lista_aux:list[int] = []
    res:int = 0
    while not c.empty():
        lista_aux.append(c.get())

    res = len(lista_aux)

    for i in range(len(lista_aux)):
        c.put(lista_aux[i])

    return res
#print(cantidad_elementos_cola(generar_nros_al_azar_cola(5,1,10)))

#EJ 15
def buscar_el_maximo_cola(c:Queue[int]) -> int:
    lista_aux:list[int] = []
    while not c.empty():
        lista_aux.append(c.get())

    valor_maximo:int = lista_aux[0]
    for i in lista_aux:
        c.put(i)
        if valor_maximo < i:
            valor_maximo = i
    return valor_maximo
#print(buscar_el_maximo_cola(generar_nros_al_azar_cola(5,1,10)))

#EJ 16.1
def armar_secuencia_de_bingo() -> Queue[int]:
    secuencia_bingo:Queue[int] = Queue()
    lista_aux:list[int] = []
    i:int = 0
    num:int = 0
    while i < 100:
        num = randint(0, 99)
        if not (num in lista_aux):
            lista_aux.append(num)
            i +=1
    for n in lista_aux:
        secuencia_bingo.put(n)
    return secuencia_bingo
#imprimir_cola(armar_secuencia_de_bingo())

#EJ 16.2
def jugar_carton_de_bingo(carton:list[int], bolillero:Queue[int]) -> int:
    jugadas:int = 0
    coincidencias:int = 0
    while coincidencias < 12:
        if bolillero.get() in carton:
            coincidencias += 1
            jugadas += 1
        else:
            jugadas += 1
    return jugadas
#print(jugar_carton_de_bingo([75,41,23,56,2,8,15,37,92,0,54,32], armar_secuencia_de_bingo()))

#EJ 17


#EJ 18 #NyA, DNI, pref, prio
def atencion_a_clientes(c:Queue[(str,int,bool,bool)]) -> Queue[(str,int,bool,bool)]:
    max_prio:Queue[(str,int,bool,bool)] = Queue()
    prio:Queue[(str,int,bool,bool)] = Queue()
    pref:Queue[(str,int,bool,bool)] = Queue()
    sin_prio:Queue[(str,int,bool,bool)] = Queue()
    orden:Queue[(str,int,bool,bool)] = Queue()

    cliente:tuple[str,int,bool,bool] = []
    while not c.empty():
        cliente = c.get()
        if cliente[2] & cliente[3]:
            max_prio.put(cliente)
        elif cliente[3]:
            prio.put(cliente)
        elif cliente[2]:
            pref.put(cliente)
        else:
            sin_prio.put(cliente)

    while not max_prio.empty():
        orden.put(max_prio.get())
    while not prio.empty():
        orden.put(prio.get())
    while not pref.empty():
        orden.put(pref.get())
    while not sin_prio.empty():
        orden.put(sin_prio.get())
    return orden

"""c:Queue[(str,int,bool,bool)] = Queue()
c.put(("A", 1, True, True))
c.put(("B", 4, True, False))
c.put(("C", 3, False, True))
c.put(("D", 2, True, True))
c.put(("E", 6, False, False))
c.put(("F", 5, True, False))
imprimir_cola(atencion_a_clientes(c))"""

#EJ 19
def agrupar_por_longitud(nombre_archivo:str) -> dict[int,int]:
    f = open(nombre_archivo)
    contenido = f.readlines()
    f.close

    d:dict[int,int] = {}
    i:int = 0
    cuento_letras:int = 0
    longitudes:list[int] = []
    
    for linea in contenido:
        i = 0
        while (i < len(linea) - 1):
            while (linea[i] != " ") and (linea[i] != "\n") and (i < len(linea) - 1):
                cuento_letras += 1
                i += 1
            if 0 < cuento_letras:
                longitudes.append(cuento_letras)
            cuento_letras = 0
            i += 1
    
    for lon in longitudes:
        d[lon] = contar_apariciones(lon, longitudes)
    return d

def contar_apariciones(i:int, longitudes:list[int]) -> int:
    aparece:int = 0
    for j in longitudes:
        if j == i:
            aparece += 1
    return aparece
#print(agrupar_por_longitud("Guia-8.txt"))

#EJ 20
def calcular_promedio_por_estudiante(nombre_archivo_notas:str) -> dict[str,float]:
    d:dict[str,float] = {}
    lista_lu:list[str] = []
    lista_lu = tomar_lu(lista_lu, nombre_archivo_notas)
    for i in range(0, len(lista_lu), 1):
        d[lista_lu[i]] = promedio_estudiante(nombre_archivo_notas, lista_lu[i])
    return d
#print(calcular_promedio_por_estudiante("Guia-8-EJ7-notas.csv"))

#EJ 21
def la_palabra_mas_frecuente(nombre_archivo:str) -> str:
    f = open(nombre_archivo)
    contenido = f.readlines()
    f.close

    apariciones_por_palabra:dict[str,int] = {}
    palabra:str = ""
    i:int = 0
    for linea in contenido:
        i = 0
        while i < len(linea) - 1:
            while (linea[i] != " ") and (linea[i] != "\n") and i < len(linea) - 1:
                palabra += linea[i]
                i += 1
            i += 1
            if palabra != "":
                if not (str(palabra) in apariciones_por_palabra.keys()):
                    apariciones_por_palabra[str(palabra)] = 1
                    palabra = ""
                else:
                    apariciones_por_palabra[str(palabra)] += 1
                    palabra = ""
    mas_frecuente:str = ""
    for p in apariciones_por_palabra.keys():
        if mas_frecuente == "":
            mas_frecuente = p
        elif apariciones_por_palabra[p] > apariciones_por_palabra[mas_frecuente]:
            mas_frecuente = p

    return mas_frecuente
#print(la_palabra_mas_frecuente("Guia-8.txt"))

#EJ 22
"""historiales:dict[str, LifoQueue[str]] = {}
historiales["Usuario_1"] = LifoQueue()
historiales["Usuario_1"].put("sitioA.com")
historiales["Usuario_1"].put("sitioB.com")
historiales["Usuario_1"].put("sitioC.com")

historiales["Usuario_2"] = LifoQueue()
historiales["Usuario_2"].put("sitioD.com")
historiales["Usuario_2"].put("sitioC.com")
historiales["Usuario_2"].put("sitioB.com")

historiales["Usuario_3"] = LifoQueue()
historiales["Usuario_3"].put("sitioC.com")
historiales["Usuario_3"].put("sitioB.com")
historiales["Usuario_3"].put("sitioD.com")"""

def visitar_sitio(historiales:dict[str, LifoQueue[str]], usuario:str, sitio:str):
    historiales[usuario].put(sitio)
    return historiales

def navegar_atras(historiales:dict[str, LifoQueue[str]], usuario:str):
    historial_invertido:list[str] = []
    while not historiales[usuario].empty():
        historial_invertido.append(historiales[usuario].get())
    
    historial_ordenado:list[str] = []
    for i in range(0, len(historial_invertido), 1):
        historial_ordenado.append(historial_invertido[len(historial_invertido) - 1 - i])
    for sitio in historial_ordenado:
        historiales[usuario].put(sitio)
    
    visitar_sitio(historiales, usuario, historial_invertido[1])

    return historiales
#navegar_atras(historiales, "Usuario_1")
#imprimir_pila(historiales["Usuario_1"])

#EJ 23
def agregar_producto(inventario:dict[str,dict[(dict[str, float], dict[str,int])]], nombre:str, precio:float, cantidad:int) -> dict[str,dict[(float, int)]]:
    inventario[nombre] = {}
    inventario[nombre]["Precio"] = precio
    inventario[nombre]["En stock"] = cantidad
    return inventario

def actualizar_stock(inventario:dict[str,dict[(dict[str, float], dict[str,int])]], nombre:str, cantidad:int) -> dict[str,dict[(float, int)]]:
    inventario[nombre]["En stock"] = cantidad
    return inventario

def actualizar_precios(inventario:dict[str,dict[(dict[str, float], dict[str,int])]], nombre:str, precio:float):
    inventario[nombre]["Precio"] = precio
    return inventario

def calcular_valor_inventario(inventario:dict[str,dict[(dict[str, float], dict[str,int])]]):
    valor_total:float = 0
    for producto in inventario.keys():
        valor_total += inventario[producto]["En stock"] * inventario[producto]["Precio"]
    return valor_total