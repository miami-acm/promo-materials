fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)
-- sum [y | x <- [1..33], let y = fib x, even y, y <= 4000000]
-- sum (filter even (takeWhile (<= 4000000) (map fib [1..])))
