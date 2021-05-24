# Calculating by recursion
def fibonacci_rec(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    return fibonacci_rec(n-1) + fibonacci_rec(n-2)


# Calculating by cached values
fibs = {0: 0, 1: 1, 2: 1}


def fib_cache(n):
    if n in fibs:
        return fibs[n]
    fibs[n] = fib_cache(n-1) + fib_cache(n-2)
    return fibs[n]


# Calculating by dynamic programming
def fib_dym(n):
    first, second = 0, 1
    for __ in range(n):
        first, second = second, first+second
    return first
