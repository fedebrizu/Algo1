--  Ej 2  --
-- 1)
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece x (y:ys) | x == y = True
                   | otherwise = pertenece x ys

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

--  Ej 3  --
-- 3)
longitud :: (Eq t) => [t] -> Int
longitud [] = 0
longitud (_:xs) = 1 + longitud xs
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

-- 9)
ordenar :: [Int] -> [Int]
ordenar (x:xs) | longitud (x:xs) == 1 = [x]
               | otherwise = ordenar (quitar (maximo (x:xs)) (x:xs)) ++ [maximo (x:xs)]
