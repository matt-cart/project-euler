import math

def isPrime(a):
    return all(a % i for i in xrange(2, a))


def findPrimes(a, b):
    primes = []
    for i in range(a, b+1):
        if isPrime(i):
            primes.append(i)
    return primes


def findFactors(n):
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0)))


def findPrimeFactors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            # "Divide AND" syntax.
            n /= d
        d = d + 1
    return factors
