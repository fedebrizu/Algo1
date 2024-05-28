import math
"""
# EJ 1.1
def imprimir_hola_mundo():
    print("¡Hola Mundo!")
imprimir_hola_mundo()
"""
"""
# EJ 1.2
def imprimir_un_verso():
    print("Sin destino y maniatado\nNi la suerte ni el pecado\nYa ni dios le cree a dios,\nSolo pido estar con vos")
imprimir_un_verso()
"""
"""
#EJ 1.3
def raizDe2():
    print(round(math.sqrt(2),3))
raizDe2()
"""

"""
#EJ 1.4
def factorial_de_dos():
    print(2)
factorial_de_dos()
"""
"""
#EJ 1.5
def perimetro():
    print(2 * math.pi)
perimetro()
"""

"""
#EJ 2.1
def imprimir_saludo(nombre:str):
    print("Hola" + ' ' + nombre)
imprimir_saludo("nombre")
"""

"""
#EJ 2.2
def raiz_cuadrada_de(numero:int):
    print(math.sqrt(numero))
raiz_cuadrada_de(2)
"""

"""
#EJ 2.3
def fahrenheit_a_celcius(t:float) -> float:
    return ((t - 32) * 5) / 9
print(fahrenheit_a_celcius (32.0))
"""

"""
#EJ 2.4
def imprimir_dos_veces(estribillo:str):
    print(estribillo * 2)
imprimir_dos_veces("...")
"""

"""
#EJ 2.5
def es_multiplo_de(n:int, m:int) -> bool:
    veo_multiplicidad:bool = False
    if (n % m == 0):
        veo_multiplicidad = True
    return veo_multiplicidad
print(es_multiplo_de (8, 2))
"""

"""
#EJ 2.6
def es_par(numero:int):
    if es_multiplo_de(numero, 2) == True:
        print("Es par")
    else:
        print("Es impar")
es_par(8)
"""

"""
#EJ 2.7
def cantidad_de_pizzas(comensales:int, min_cant_de_porciones) -> int:
    return math.ceil(comensales * min_cant_de_porciones / 8)
print(cantidad_de_pizzas (5, 7))
"""

"""
#EJ 3.1
def alguno_es_0(x:float, y:float) -> bool:
    hay_un_cero:bool = False
    hay_un_cero = (x + y == x | y)
    return hay_un_cero
print(alguno_es_0(0, 5))
"""

"""
#EJ 3.2
def ambos_son_0(x:float, y:float) -> bool:
    ambos_ceros:bool = False
    ambos_ceros = (x + y == x) & (x + y == y)
    return ambos_ceros
print(ambos_son_0(0, 5))
"""

"""
#EJ 3.3
def es_nombre_largo(nombre:str) -> bool:
    nombre_largo:bool = False
    nombre_largo = (len(nombre) >= 3) & (len(nombre) <= 8)
    return nombre_largo
print(es_nombre_largo("Federico"))
"""

"""
#EJ 3.4
def es_bisiesto(n:int) -> bool:
    tiene_366_dias:bool = False
    tiene_366_dias = ((n % 4 == 0) & (n % 100 != 0)) | (n % 400 == 0)
    return tiene_366_dias
print(es_bisiesto(700))
"""

#EJ 4.1


"""
#problema suma total (in s:seq<Z>) : Z {
#requiere: {True}
#asegura: {res es la suma de todos los elementos de s}
#}
def suma_total_for(s: list[int]) -> int:
    suma: int = 0
    for i in s:
        suma += i
    return suma
print (suma_total_for([2,4,4]))
"""

"""
def suma_total_while(s: list[int]) -> int:
    suma: int = 0
    i: int = 0
    while i < len(s):
        suma += s[i]
        i+=1
    return suma
print (suma_total_while([2,4,4]))
"""

"""
#problema pertenece (in s:seq<Z>, in e: Z) : Bool {
#requiere: {True}
#asegura: {(res = true) ↔ e ∈ s}
#}

def pertenece_1 (s:list[int], e:int) -> bool:
    for i in s:
        if (e == i):
            return True
    return False
#print(pertenece_1([1,2,3,4,5], 1))
"""

"""
def pertenece_2 (s:list[int], e:int) -> bool:
    lo_encontre: bool = False
    for i in s:
        if i == e:
            lo_encontre = True
    return lo_encontre
print(pertenece_2([1,2,3,4,5], 1))
"""

"""
def pertenece_3 (s:list[int], e:int) -> bool:
    lo_encontre: bool = False
    i: int = 0
    while i < len(s) and not lo_encontre:
        if e == s[i]:
            lo_encontre = True
        i += 1
    return lo_encontre
print(pertenece_3([1,2,3,4,5], 6))
"""

"""
def pertenece_4 (s:list[int], e:int) -> bool:
    lo_encontre: bool = False
    for i in range (0, len(s), 1):
        if i == e:
            lo_encontre = True
    return lo_encontre
print(pertenece_4([1,2,3,4,5], 8))
"""

"""
def fortaleza_de_una_contra (cont:str) -> str:
    seguridad:str = "Amarillo"
    hay_minuscula:bool = False
    hay_mayus:bool = False
    hay_numero:bool = False

    if len(cont) < 5:
        seguridad = "Rojo"
    
    if len(cont) > 8:
        for i in cont:
            if (i >= 'a' and i <= 'z' and not hay_minuscula):
                hay_minuscula = True
            if (i >= 'A' and i <= 'Z' and not hay_mayus):
                hay_mayus = True
            if (i >= '0' and i <= '9' and not hay_numero):
                hay_numero = True

    if (hay_minuscula and hay_mayus and hay_numero):
        seguridad = "Verde"
    return seguridad
print (fortaleza_de_una_contra("123456aAl"))
"""

"""
def pertenece_a_cada_uno_v2 (s:list[list[int]], e:int, res:list[bool]):
    res.clear
    for i in range (0,len(s),1):
        res.append (pertenece_1 (s[i], e))

res:list[bool] = []
pertenece_a_cada_uno_v2 ([[1],[1,2],[1,2,3]], 1, res)
print (res)
"""
