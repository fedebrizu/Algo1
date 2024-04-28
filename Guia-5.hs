--  Ej 1  --
-- 1)
longitud :: (Eq t) => [t] -> Int
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

-- 2)
ultimo :: (Eq t) => [t] -> t
ultimo [x] = x
ultimo (x:xs) = ultimo xs

-- 3)
principio :: (Eq t) => [t] -> [t]
principio [x] = []
principio (x:xs) = (x : principio xs)

-- 4)
reverso :: (Eq t) => [t] -> [t]
reverso [x] = [x]
reverso (x:xs) = reverso xs ++ [x]
------------

--  Ej 2  --
-- 1)
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece x (y:ys) | x == y = True
                   | otherwise = pertenece x ys

-- 2)
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [x] = True
todosIguales (x:y:xs) | x == y = todosIguales (y:xs)
                      | otherwise = False

-- 3)
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos (x:xs) | pertenece x xs = False
                      | otherwise = todosDistintos xs

-- 4)
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) | pertenece x xs == True = True
                    | otherwise = hayRepetidos xs

-- 5)
quitar :: (Eq t) => t -> [t] -> [t] --saca la primer aparicion de un elemento de una lista dada 
quitar t lista  | pertenece t lista == False = lista
                | t == head lista = tail lista
                | otherwise = [head lista] ++ quitar t (tail lista)

-- 6)
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos x (y:ys) | pertenece x (y:ys) == True = quitarTodos x (quitar x (y:ys))
                     | otherwise = (y:ys)

-- 7)
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) | pertenece x xs == True = [x] ++ eliminarRepetidos (quitarTodos x xs)
                         | otherwise = [x] ++ eliminarRepetidos xs

-- 8)
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos [] [] = True
mismosElementos _ [] = False
mismosElementos [] _ = False
mismosElementos (x:xs) (y:ys) | pertenece x (y:ys) == True = mismosElementos (quitarTodos x xs)  (quitarTodos x (y:ys))

-- 9)
capicua :: (Eq t) => [t] -> Bool
capicua [] = True
capicua [x] = True
capicua lista | head lista == ultimo lista = capicua (tail (principio lista))
              | otherwise = False
------------

--  Ej 3  --
-- 1)
sumatoria :: [Int] -> Int
sumatoria [x] = x
sumatoria (x:xs) = x + sumatoria xs

productoria :: [Int] -> Int
productoria [x] = x
productoria (x:xs) = x * productoria xs

-- 3)
{-
maximo :: [Int] -> Int
maximo (x:xs) | longitud (x:xs) == 1 = x
              | x <= head(xs) = maximo xs
              | otherwise = maximo (x:quitar (head xs) xs)
-}
maximo :: [Int] -> Int
maximo [x] = x
maximo (x:y:xs) | x <= y = maximo (y:xs)
                | otherwise = maximo (x:xs)

-- 4)
sumarN :: Int -> [Int] -> [Int]
sumarN n [x] = [n + x]
sumarN n (x:xs) = [n + x] ++ sumarN n xs

-- 5)
sumarElPrimero :: [Int] -> [Int]
sumarElPrimero [] = []
sumarElPrimero (x:xs) = sumarN x (x:xs)

--6)
sumarElUltimo :: [Int] -> [Int]
sumarElUltimo [] = []
sumarElUltimo seq = sumarN (ultimo seq) seq

-- 7)
pares :: [Int] -> [Int]
pares [] = []
pares (x:xs) | mod x 2 == 0 = [x] ++ pares xs
             | otherwise = pares xs

-- 8)
multiplosDeN :: Int -> [Int] -> [Int]
multiplosDeN _ [] = []
multiplosDeN n (x:xs) | mod x n == 0 = [x] ++ multiplosDeN n xs
                      | otherwise = multiplosDeN n xs

-- 9)
ordenar :: [Int] -> [Int]
ordenar (x:xs) | longitud (x:xs) == 1 = [x]
               | otherwise = ordenar (quitar (maximo (x:xs)) (x:xs)) ++ [maximo (x:xs)]
------------

--  Ej 4  --
-- a)
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:y:xs) | x == ' ' && y == ' ' = sacarBlancosRepetidos (quitar ' ' (x:y:xs))
                               | otherwise = [x] ++ sacarBlancosRepetidos (y:xs)

-- b)
contarPalabras :: [Char] -> Int
contarPalabras [] = 0
contarPalabras (x:xs) | pertenece ' ' (x:xs) == False = 1
                      | x == ' ' = 1 + contarPalabras xs
                      | otherwise = contarPalabras xs

-- c)
palabras :: [Char] -> [[Char]]
palabras [] = []
palabras (x:xs) = [primeraPalabra (x:xs)] ++ palabras (quitarPrimerasNPalabras (x:xs) 1)

primeraPalabra :: [Char] -> [Char]
primeraPalabra [] = []
primeraPalabra (x:xs) | pertenece ' ' (x:xs) == False = (x:xs)
                      | x == ' ' = []
                      | otherwise = [x] ++ primeraPalabra xs

quitarPrimerasNPalabras :: [Char] -> Int -> [Char]
quitarPrimerasNPalabras [] _ = [] 
quitarPrimerasNPalabras (x:xs) n | n >= contarPalabras (x:xs) = []
                                 | n == 0 = (x:xs)
                                 | x == ' ' = quitarPrimerasNPalabras xs (n-1)
                                 | otherwise = quitarPrimerasNPalabras xs n
------------

-- d)
palabraMasLarga :: [Char] -> [Char]
palabraMasLarga [] = []
palabraMasLarga lista | contarPalabras lista == 1 = quitar ' ' lista
                      | longitud (primeraPalabra lista) >= longitud (primeraPalabra (quitarPrimerasNPalabras lista 1)) = palabraMasLarga ((primeraPalabra lista) ++ [' '] ++ quitarPrimerasNPalabras lista 2)
                      | otherwise = palabraMasLarga (quitarPrimerasNPalabras lista 1)

-- e)
aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (x:xs) = x ++ aplanar xs

-- f)
aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [x] = x
aplanarConBlancos (x:xs) = x ++ [' '] ++ aplanarConBlancos xs

-- g)
aplanarConNBlancos :: [[Char]] -> Int -> [Char]
aplanarConNBlancos [x] _ = x
aplanarConNBlancos (x:xs) n = x ++ completarBlancos n ++ aplanarConNBlancos xs n

completarBlancos :: Int -> [Char]
completarBlancos 0 = []
completarBlancos n = [' '] ++ completarBlancos (n-1)
------------

--  Ej 5  --
-- 1)
sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [x] = [x]
sumaAcumulada (x:y:xs) = [x] ++ sumaAcumulada ((x+y):xs)

-- 2)
descomponerEnPrimos :: [Int] -> [[Int]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) = (descomposicionInterna x) : descomponerEnPrimos xs

descomposicionInterna :: Int -> [Int]
descomposicionInterna n | esPrimo n == True = [n]
                        | otherwise = [menorDivisor n] ++ descomposicionInterna (div n (menorDivisor n))
--aux de guia 4
menorDivisor :: Int -> Int --sin contar el 1
menorDivisor n = primerDivisorDesde n 2
--aux de guia 4
primerDivisorDesde :: Int -> Int -> Int -- devuelve el primer divisor que encuentre de n, desde k (con k<=n)
primerDivisorDesde n k | k == n = n
                       | mod n k == 0 = k
                       | otherwise = primerDivisorDesde n (k+1)
--aux de guia 4
esPrimo :: Int -> Bool
esPrimo n = menorDivisor n == n
------------