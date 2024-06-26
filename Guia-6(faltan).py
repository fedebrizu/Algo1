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

"""
#EJ 4.1
def peso_pino(altura:float) -> float:
    peso:float = 0
    if (altura < 300):
        peso = 3 * altura
    else:
        peso = 900 + 2 * (altura - 300)
    return peso

#EJ 4.2
def es_peso_util(peso:float) -> bool:
    peso_util:bool = False
    if ((peso >= 400) & (peso <= 1000)):
        peso_util = True
    return peso_util

#EJ 4.3
def sirve_pino_extended_edition(altura:float) -> bool:
    sirve:bool = False
    peso:float = 0
    
    if (altura < 300):
        peso = 3 * altura
    else:
        peso = 900 + 2 * (altura - 300)
        
    if ((peso >= 400) & (peso <= 1000)):
        sirve = True
    return sirve

#EJ 4.4
def sirve_pino_resumida(altura:float) -> bool:
    sirve:bool = False
    sirve = es_peso_util(peso_pino(altura))
    return sirve
print(sirve_pino_resumida(1000))
"""

"""
#EJ 6.1
def cuenta_hasta_diez():
    i:int = 1
    while i <= 10:
        print(i)
        i += 1
cuenta_hasta_diez()
"""

"""
#EJ 6.2
def pares_entre_10_y_40():
    i:int = 10
    while i <= 40:
        print(i)
        i += 2
pares_entre_10_y_40()
"""

"""
#EJ 6.3
def eco():
    i:int = 1
    while i <= 10:
        print("eco")
        i += 1
eco()
"""

"""
#EJ 6.4
def cuenta_despegue(contador:int):
    while contador > 0:
        print(contador)
        contador -= 1
    print("Despegue")
cuenta_despegue(5)
"""

"""
#EJ 6.5
def viaje_al_pasado(partida:int, llegada:int):
    while partida > llegada:
        partida -= 1
        print("Viajó un año al pasado, estamos en el año", (partida))
viaje_al_pasado(5, 1)
"""
