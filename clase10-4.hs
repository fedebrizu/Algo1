todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor x y | (fst y > fst x) && (snd y > snd x) = True
              | otherwise = False

posPrimerPar :: (Int, Int, Int) -> Int
posPrimerPar (a, b, c) | mod a 2 == 0 = 1
                       | mod b 2 == 0 = 2
                       | mod c 2 == 0 = 3
                       | otherwise = 4

bisiesto :: Int -> Bool
bisiesto a | mod a 400 == 0 = True
           | mod a 100 == 0 = False
           | mod a 4 == 0 = True
           | otherwise = False

modulo :: Float -> Float
modulo x | x <= 0 = -x
         | otherwise = x

distanciaManhattan :: (Float , Float, Float) -> (Float , Float, Float) -> Float
distanciaManhattan (x1, x2, x3) (y1, y2, y3) = modulo (x1 - y1) + modulo (x2 - y2) + modulo (x3 - y3)

estanRelacionados :: Int -> Int -> Bool
estanRelacionados a b = mod (a*a) (a*b) == 0

sumarMultiplos :: (Int, Int, Int) -> Int -> Int
sumarMultiplos (a, b, c) n | mod a n == 0 && mod b n == 0 && mod c n == 0 = a + b + c
                           | mod a n == 0 && mod b n == 0 = a + b
                           | mod a n == 0 && mod c n == 0 = a + c
                           | mod b n == 0 && mod c n == 0 = b + c
                           | mod a n == 0 = a
                           | mod b n == 0 = b
                           | mod c n == 0 = c
                           | otherwise = 0