parteEntera :: Float -> Int
parteEntera x | x >= 0 && x < 1 = 0
              | x >= 1 = parteEntera(x-1) + 1
              | x < 0 = parteEntera(x+1) - 1

esDivisible :: Int -> Int -> Bool
esDivisible n m | m == 0 = False
                | n == 0 = True
                | m > n = False
                | otherwise = esDivisible (n-m) m

sumaImpares :: Int -> Int
sumaImpares n | n == 0 || n == 1 = n
              | otherwise = 2*n - 1 + sumaImpares(n-1)

medioFact :: Int -> Int
medioFact n | n == 0 || n == 1 = 1
            | otherwise = n * medioFact(n-2)

sumaDigitos :: Int -> Int
sumaDigitos n | n < 10 = n
              | otherwise = mod n 10 + sumaDigitos(div n 10)

todosDigitosIguales :: Int -> Bool
todosDigitosIguales n | n < 10 = True
                      | mod n 10 - mod (div n 10) 10 == 0 = todosDigitosIguales(div n 10)
                      | otherwise = False

cantDigitos :: Int -> Int
cantDigitos n | n < 10 = 1 
              | otherwise = 1 + cantDigitos(div n 10)


iesimoDigito :: Int -> Int -> Int
iesimoDigito n m | m < cantDigitos(n) = iesimoDigito(div n 10) m 
                 | otherwise = mod n 10


