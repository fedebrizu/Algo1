--  Ej 1  --
fibonacci :: Int -> Int
fibonacci n | n == 0 || n == 1 = n
            | otherwise = fibonacci(n-1) + fibonacci(n-2)

--  Ej 2  --
parteEntera :: Float -> Int
parteEntera x | x >= 0 && x < 1 = 0
              | x >= 1 = parteEntera(x-1) + 1
              | x < 0 = parteEntera(x+1) - 1

-- Ej 3  --
esDivisible :: Int -> Int -> Bool
esDivisible n m | m == 0 = False
                | n == 0 = True
                | m > n = False
                | otherwise = esDivisible (n-m) m

-- Ej 4  --
sumaImpares :: Int -> Int
sumaImpares n | n == 0 || n == 1 = n
              | otherwise = 2*n - 1 + sumaImpares(n-1)

--  Ej 5  --
medioFact :: Int -> Int
medioFact n | n == 0 || n == 1 = 1
            | otherwise = n * medioFact(n-2)

--  Ej 6  --
sumaDigitos :: Int -> Int
sumaDigitos n | n < 10 = n
              | otherwise = mod n 10 + sumaDigitos(div n 10)

--  Ej 7  --
todosDigitosIguales :: Int -> Bool
todosDigitosIguales n | n < 10 = True
                      | mod n 10 - mod (div n 10) 10 == 0 = todosDigitosIguales(div n 10)
                      | otherwise = False

--  Ej 8  --
cantDigitos :: Int -> Int
cantDigitos n | n < 10 = 1
              | otherwise = 1 + cantDigitos(div n 10)


iesimoDigito :: Int -> Int -> Int
iesimoDigito n m | m < cantDigitos(n) = iesimoDigito(div n 10) m 
                 | otherwise = mod n 10
-------------

--  Ej 9  -- (no anda para casos como el 1021)
potenciaDeN :: Int -> Int -> Int
potenciaDeN n m | m == 0 = 1
                | otherwise = n * potenciaDeN n (m-1)

esCapicua :: Int -> Bool
esCapicua n | cantDigitos n == 1 = True
            | iesimoDigito n 1 - mod n 10 == 0 = --veo si son iguales el primer y el último dígito
            esCapicua (div (mod n (potenciaDeN 10 (cantDigitos(n) - 1))) 10)
            | otherwise = False
-------------

--  Ej 10  --
-- a) (2^n+1) - 1
f1 :: Int -> Int
f1 n | n == 0 = 1
     | otherwise = potenciaDeN 2 n + f1 (n-1)

-- b) ((q^n+1) - 1) / (q - 1)
f2 :: Int -> Int -> Int
f2 n q | n == 0 = 1
       | otherwise = potenciaDeN q n + f2 (n-1) q

-- c) ((q^2n+1) - 1) / (q - 1)
f3 :: Int -> Int -> Int
f3 n q = f2(2*n) q

-- d) ((q^2n+1) - (q^n+1)) / (q - 1)
f4 :: Int -> Int -> Int
f4 n q = f2(2*n) q - f2(n) q

--  Ej 11  --
factorial :: Int -> Int
factorial n | n == 0 = 1
            | otherwise = n * factorial(n-1)

eAprox :: Int -> Float
eAprox n | n == 0 = 1
         | otherwise = 1 / (fromIntegral (factorial (n))) + eAprox (n-1) -- fromIntegral es una función propia de Haskell