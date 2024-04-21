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
iesimoDigito n m | m < cantDigitos n = iesimoDigito(div n 10) m 
                 | otherwise = mod n 10
-------------

--  Ej 9  --
esCapicua :: Int -> Bool
esCapicua n | n < 10 = True
            | comparacionDigitos n (cantDigitos n) == comparacionDigitos n ((cantDigitos n) - 1) = True
            | otherwise = False

comparacionDigitos :: Int -> Int -> Bool
comparacionDigitos n pos | pos == 1 && mod n 10 == div n 10 = True
                         | iesimoDigito n pos == iesimoDigito n (cantDigitos (n) - pos + 1) = True --evalúa por izquierda y por derecha
                         | otherwise = False
-------------

--  Ej 10  --
-- a) (2^n+1) - 1
f1 :: Int -> Int
f1 n | n == 0 = 1
     | otherwise =  2 ^ n + f1 (n-1)

-- b) ((q^n+1) - 1) / (q - 1)
f2 :: Int -> Int -> Int
f2 n q | n == 0 = 1
       | otherwise =  q ^ n + f2 (n-1) q

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
         | otherwise = 1 / (fromIntegral (factorial (n))) + eAprox (n-1) -- fromIntegral es una función ya definida de Haskell
-------------

--  Ej 12  --
sucesionRaizDe2 :: Int -> Float
sucesionRaizDe2 n | n == 1 = 2
                  | otherwise = 2 + 1 / sucesionRaizDe2 (n-1)

raizDe2Aprox :: Int -> Float
raizDe2Aprox n | n == 0 = 0
               | n == 1 = 1
               | otherwise = sucesionRaizDe2 (n) - 1
-------------

--  Ej 13  --
sumaDoble :: Int -> Int -> Int
sumaDoble n m | n == 0 = 0
              | otherwise = sumaInterna n m + sumaInterna (n-1) m

sumaInterna :: Int -> Int -> Int
sumaInterna i j | j == 1 = i
                | otherwise = i ^ j + sumaInterna i (j-1)
-------------

--  Ej 14  --
sumaPotencias :: Int -> Int -> Int -> Int
sumaPotencias q n m = q ^ (combinacionesDeSuma n m)

combinacionesDeSuma :: Int -> Int -> Int
combinacionesDeSuma n m | n == 1 = sumaAB n m
                        | otherwise = sumaAB n m + combinacionesDeSuma (n-1) m

sumaAB :: Int -> Int -> Int 
sumaAB a b | b == 1 = a + b
           | otherwise = a + b + sumaAB a (b-1)
-------------

--  Ej 15  --
sumaRacionales :: Int -> Int -> Float
sumaRacionales n m | n == 1 = sumaRacInterna n m
                   | otherwise = sumaRacInterna n m + sumaRacionales (n-1) m

sumaRacInterna :: Int -> Int -> Float
sumaRacInterna p q | q == 1 = fromIntegral p / fromIntegral q
                   | otherwise = fromIntegral p / fromIntegral q + sumaRacInterna p (q-1)
-------------

--  Ej 16  --
-- a)
menorDivisor :: Int -> Int --sin contar el 1
menorDivisor n = primerDivisorDesde n 2

primerDivisorDesde :: Int -> Int -> Int -- devuelve el primer divisor que encuentre de n, desde k (con k<=n)
primerDivisorDesde n k | k == n = n
                       | mod n k == 0 = k
                       | otherwise = primerDivisorDesde n (k+1)

-- b)
esPrimo :: Int -> Bool
esPrimo n = menorDivisor n == n

-- c)
sonCoprimos :: Int -> Int -> Bool
sonCoprimos n m = comparaDivisores n m 2

comparaDivisores :: Int -> Int -> Int -> Bool
comparaDivisores n m k | primerDivisorDesde n k == primerDivisorDesde m k = False 
                       | k >= n || k >= m = True
                       | otherwise = comparaDivisores n m (k+1)

-- d)
nEsimoPrimo :: Int -> Int
nEsimoPrimo n = cuentaPrimos n 3 1

cuentaPrimos :: Int -> Int -> Int -> Int --cuenta la cantidad de numeros primos (n), empezando desde k
cuentaPrimos n k j | j == n = k-1
                   | esPrimo k == True = cuentaPrimos n (k+1) (j+1) --j cuenta los numeros primo registrados
                   | otherwise = cuentaPrimos n (k+1) j --hace recursión sobre k nada más
-------------

--  Ej  17  --
esFibonacci :: Int -> Bool
esFibonacci n = recorreFibonacci n 1

recorreFibonacci :: Int -> Int -> Bool --detecta si el numero q recibe pertenece al fibonacci de algún k
recorreFibonacci n k | fibonacci k > n = False
                     | fibonacci k == n = True
                     | otherwise = recorreFibonacci n (k+1)
-------------

--  Ej 18  --
mayorDigitoPar :: Int -> Int
mayorDigitoPar n = deteccionMayorPar n (cantDigitos n) (-1)

deteccionMayorPar :: Int -> Int -> Int -> Int
deteccionMayorPar n k p | k == 0 = p
                        | mod (iesimoDigito n k) 2 == 0 && iesimoDigito n k > p = deteccionMayorPar n (k-1) (iesimoDigito n k)
                        | otherwise = deteccionMayorPar n (k-1) p
-------------

--  Ej 19  --
esSumaInicialDePrimos :: Int -> Bool
esSumaInicialDePrimos n = recorrePrimos n 1 0

recorrePrimos :: Int -> Int -> Int -> Bool
recorrePrimos n k s | n < 2 = False
                    | n < s = False
                    | n == s = True
                    | otherwise = recorrePrimos n (k+1) (s + nEsimoPrimo k)
-------------

--  Ej 20  --
tomaValorMax :: Int -> Int -> Int 
tomaValorMax n1 n2 = sumaDivisores n1 (n2 - n1) 1

sumaDivisores :: Int -> Int -> Int -> Int
sumaDivisores m k i | k == 0 = m
                    | todosLosDivisores m 1 > todosLosDivisores (m + i) 1 = sumaDivisores m (k-1) (i+1)
                    | todosLosDivisores m 1 < todosLosDivisores (m + i) 1 = sumaDivisores (m + i) (k-1) 1

todosLosDivisores :: Int -> Int -> Int --devuelve la suma de todos los divisores de n, empezando en k
todosLosDivisores n k | k == n = k
                      | mod n k == 0 = k + todosLosDivisores n (k+1)
                      | otherwise = todosLosDivisores n (k+1)
-------------

--  Ej 21  --
pitagoras :: Int -> Int -> Int -> Int
pitagoras m n r = totalParesPQ m n r 0

totalParesPQ :: Int -> Int -> Int -> Int -> Int
totalParesPQ p q r i | p < 0 = i
                     | otherwise = totalParesPQ (p-1) q r (i + totalParesInterna p q r 0)

totalParesInterna :: Int -> Int -> Int -> Int -> Int
totalParesInterna p q r j | q < 0 = j
                          | p^2 + q^2 <= r^2 = totalParesInterna p (q-1) r (j+1)
                          | otherwise = totalParesInterna p (q-1) r j
-------------