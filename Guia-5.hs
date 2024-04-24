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
contarPalabras [] = 1
contarPalabras (x:xs) | x == ' ' = 1 + contarPalabras xs
                      | otherwise = contarPalabras xs

-- c)
{-
palabras :: [Char] -> [[Char]]
palabras [x] = [[x]]
palabras (x:xs) | x /= ' ' = [[x]] ++ palabras xs
                | otherwise = palabras xs
-}

-- d)
{-
palabraMasLarga :: [Char] -> [Char]
palabraMasLarga [] = []
palabraMasLarga (x:y:xs) | 
-}