import math
import random
import numpy as np
#Primera Parte:
"""
#EJ 1.1
def pertenece(s:list[int], e:int) -> bool:
    for i in s:
        if i == e:
            return True
    return False
#print(pertenece([1,2,3], 1))
"""

"""
#EJ 1.2
def divide_a_todos(s:list[int], e:int) -> bool:
    for i in s:
        if (i % e != 0):
            return False
    return True
print(divide_a_todos([2,4,6,8], 2))
"""

"""
#EJ 1.3
def suma_total(s:list[int]) -> bool:
    suma = 0
    for i in s:
        suma += i
    return suma
print(suma_total([1,2,3,4]))
"""

"""
#EJ 1.4
def ordenados(s:list[int]) -> bool:
    for i in range (1, len(s), 1):
        if s[i-1] > s[i]:
            return False
    return True
#print(ordenados([1,4,4,4,5]))
"""

"""
#EJ 1.5
def alguna_mas_de_7(s:list[str]) -> bool:
    for i in s:
        if len(i) > 7:
            return True
    return False
print(alguna_mas_de_7(["hola","que","tal"]))
"""

"""
#EJ 1.6
def es_palindromo(p:str) -> bool:
    j:int = 0
    for i in range (0, len(p)//2, 1):
        if p[i] != p[len(p)-1-i]:
            return False
    return True
print(es_palindromo("aaaaa"))
"""

"""
#EJ 1.7
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
#EJ 1.8
def saldo_actual(movimientos:list[(str,float)]):
    saldo = 0
    for i in movimientos:
        if i[0] == "I":
            saldo += i[1]
        elif i[0] == "R":
            saldo -= i[1]
    return saldo
print(saldo_actual([("I", 2000), ("R", 20),("R", 1000),("I", 300)]))
"""

"""
#EJ 1.9
def tres_vocales(p:str) -> bool:
    vocales_distintas:int = 0
    tieneA:bool = False
    tieneE:bool = False
    tieneI:bool = False
    tieneO:bool = False
    tieneU:bool = False

    for i in p:
        if ((i == "a" or i == "A") & (not tieneA)):
            vocales_distintas += 1
            tieneA = True

        if ((i == "e" or i == "E") & (not tieneE)):
            vocales_distintas += 1
            tieneE = True
        
        if ((i == "i" or i == "I") & (not tieneI)):
            vocales_distintas += 1
            tieneI = True
        
        if ((i == "o" or i == "O") & (not tieneO)):
            vocales_distintas += 1
            tieneO = True
        
        if ((i == "u" or i == "U") & (not tieneU)):
            vocales_distintas += 1
            tieneU = True
    if vocales_distintas >= 3:
        return True
    return False
print(tres_vocales("AeI"))
"""

#Segunda Parte:
"""
#EJ 2.1
def pos_par_en_0_inout(s:list[int]) -> list[int]:
    for i in range(0, len(s), 2):
        s[i] = 0
    return s
print(pos_par_en_0_inout([1,2,5,3,7,1,3,7,3,2,9]))
"""

"""
#EJ 2.2
def pos_par_en_0_in(s:list[int]) -> list[int]:
    res:list[int] = []
    for i in range(0, len(s), 1):
        if i % 2 == 0:
            res.append(0)
        else:
            res.append(s[i])
    return res
print(pos_par_en_0_in([1,2,5,3,7,1,3,7,3,2,9]))
"""

"""
#EJ 2.3
def sin_vocales(s:str) -> str:
    res:str = []
    for c in s:
        if not ((c == "a") | (c == "e") | (c == "i") | (c == "o") | (c =="u") | (c == "A") | (c == "E") | (c == "I") | (c == "O") | (c =="U")):
            res.append(c)
    return res
print(sin_vocales("Federico"))
"""

"""
#EJ 2.4
def reemplaza_vocales(s:str) -> str:
    res:str = []
    for c in s:
        if ((c == "a") | (c == "e") | (c == "i") | (c == "o") | (c =="u") | (c == "A") | (c == "E") | (c == "I") | (c == "O") | (c =="U")):
            res.append("_")
        else:
            res.append(c)
    return res
print(reemplaza_vocales("Federico"))
"""

"""
#EJ 2.5
def da_vuelta_str(s:str) -> str:
    res:str = []
    for i in range(0, len(s), 1):
        res.append(s[len(s) - 1 - i])
    return res
print(da_vuelta_str("Federico"))
"""

"""
#EJ 2.6
def eliminar_repetidos(s:str) -> str:
    for caracter in s:
        if contar_apariciones(caracter, s) > 1:
            s = eliminar_repetidos_aux(caracter, s)
    return s

def contar_apariciones(caracter:str, s:str) -> int:
    apariciones = 0
    for c in s:
        if c == caracter:
            apariciones += 1
    return apariciones

def eliminar_repetidos_aux(caracter:str, s:str) -> str:
    res:str = []
    ya_aparecio:bool = False
    for c in s:
        if (c == caracter) & (not ya_aparecio):
            ya_aparecio = True
            res.append(c)
        if (c != caracter):
            res.append(c)
    return res
print(eliminar_repetidos("Federico"))
"""

"""
#EJ 3
def aprobado(notas:list[int]) -> int:
    res:int = 3
    if todo_aprobado(notas) & (promedio(notas) >= 7.00):
        res = 1
    elif todo_aprobado(notas) & (4.00 <= promedio(notas)) & (promedio(notas) <= 7.00):
        res = 2
    return res

def todo_aprobado(notas:list[int]) -> bool:
    for n in notas:
        if n < 4:
            return False
    return True

def promedio(notas:list[int]) -> float:
    suma:int = 0
    prom:float = 0
    for n in notas:
        suma += n
    prom = suma / len(notas)
    return prom

print(aprobado([6,5,9,4,6,4,8]))
"""

"""
#EJ 4.1
def nombres() -> list[str]:
    estudiante:str = []
    lista_nombres:list[str] = []
    while (estudiante != "listo"):
        if (estudiante != []):
            lista_nombres.append(estudiante)
        estudiante = input('->')
    return lista_nombres
print(nombres())
"""

"""
#EJ 4.2
def monedero() -> list[(str,str)]:
    historial:list[(str,str)] = []
    accion:str = []
    while (accion != "X"):
        if accion == "C":
            historial.append(("C",input('Monto-> ')))
        if accion == "D":
            historial.append(("D",input('Monto-> ')))
        accion = input('Accion-> ')
    return historial
print(monedero())
"""

"""
#EJ 4.3
def siete_y_medio() -> list[str]:
    mazo:list[int] = [1,2,3,4,5,6,9,10,11,12] 
    suma_valores:float = 0
    accion = []
    historial:list[str] = []

    while (suma_valores < 7.5) & (accion != "P"):
        if (historial == []):
            accion = input('<<Tome una carta (T) para iniciar>> -> ')
        else:
            accion = input('¿Tomar otra (T) o plantarse (P)? -> ')
        if (accion == "T"):
            carta_tomada = random.choice(mazo)
            if (carta_tomada > 9):
                suma_valores += 0.5
            else:
                suma_valores += carta_tomada
            print(".Tomó un: " + str(carta_tomada) + ", su suma es de: " + str(suma_valores))
            historial.append(carta_tomada)

    if (suma_valores > 7.5):
        print("- Perdió, la suma superó los 7.5")
    if (accion == "P"):
        print("- Se plantó con " + str(suma_valores))
    if (suma_valores == 7.5):
        print("- ¡Ganó! llegó al valor exacto")
    return historial
siete_y_medio()
"""

"""
#EJ 5.1
def pertenece_a_cada_uno_version_1(s:list[list[int]], e:int, res:list[bool]):
    res.clear()
    for i in s:
        if (pertenece(i, e)):
            res.append(True)
        else:
            res.append(False)
    return res
res = []
print(pertenece([1,3,5,2,4], 5))
print(pertenece_a_cada_uno_version_1(([1,3,5,2,4],[2,4,7,1],[8,2,4,9,1],[3,5,4,1],[1,3,2,5]), 5, res))
"""

"""
#EJ 5.2
def pertenece_a_cada_uno_version_2(s:list[list[int]], e:int, res:list[bool]):
    res.clear()
    for i in s:
        if (pertenece(i, e)):
            res.append(True)
        else:
            res.append(False)
    return res
"""

"""
#EJ 5.3
def es_matriz(s:list[list[int]]) -> bool:
    res:bool = True
    if s == []:
        res = False
    else:
        for fila in s:
            if len(fila) != len(s[0]):
                res = False
    return res
print(es_matriz(([4,2,1],[5,3,1],[1,5,9])))
"""

"""
#EJ 5.4
def filas_ordenadas(s:list[list[int]], res:list[bool]):
    res.clear()
    for fila in s:
        if ordenados(fila):
            res.append(True)
        else:
            res.append(False)
    return res
res = []
print(filas_ordenadas(([4,2,1],[5,3,1],[1,5,9]), res))
"""

"""
#EJ 5.5
def elevar_matriz(d:int, p:int) -> list[list[int]]:
    m:list[list[int]] = np.random.randint(0,10,(d,d))

    i:int = 0
    while i < p:
        res = multiplicacion_de_matrices_cuadradas(d, m, m)
        i+=1
    return res

def multiplicacion_de_matrices_cuadradas (dim:int, m1:list[list[int]], m2:list[list[int]]) -> list[list[int]]:
    i:int = 0
    j:int = 0
    k:int = 0
    res:list[list[int]] = np.random.randint(0,1,(dim,dim))
    suma:int = 0

    while i < dim:
        while j < dim:
            while k < dim:
                suma += (m1[i][k] * m2[k][j])
                k += 1
            k = 0
            res[i][j] = suma
            suma = 0
            j += 1
        j = 0
        i += 1
    return res

print(elevar_matriz(3, 2))
"""