#46) Goldbach's other conjecture
#It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#9 = 7 + 2×1^2
#15 = 7 + 2×2^2
#21 = 3 + 2×3^2
#25 = 7 + 2×3^2
#27 = 19 + 2×2^2
#33 = 31 + 2×1^2
#It turns out that the conjecture was false.
#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

#%% Solution
from math import sqrt

def primes(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]

def is_combi(n, p):
    return sqrt((n-p)/2)%1 == 0

def is_goldbach(n):
    return any([is_combi(n, p) for p in primes(n)])

N = 10000
list_primes = list(primes(N))
list_composites = [x for x in range(3, N, 2) if x not in list_primes]
list_false = [x for x in list_composites if not is_goldbach(x)]

list_false[0]
