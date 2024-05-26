"""
# EJ 1
def imprimir_hola_mundo ():
    print("¡Hola Mundo!")
imprimir_hola_mundo()
"""
"""
# EJ 2
def imprimir_un_verso ():
    print ("Sin destino y maniatado\nNi la suerte ni el pecado\nYa ni dios le cree a dios,\nSolo pido estar con vos")
imprimir_un_verso ()
"""



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