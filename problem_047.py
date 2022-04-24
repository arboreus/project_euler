#47) Distinct primes factors
#The first two consecutive numbers to have two distinct prime factors are:
#14 = 2 × 7
#15 = 3 × 5
#The first three consecutive numbers to have three distinct prime factors are:
#644 = 2^2 × 7 × 23
#645 = 3 × 5 × 43
#646 = 2 × 17 × 19.
#Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?

#%% Solution
from re import search

def primes(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]

def get_factors(n, f):
    if str(n) in f:
        return f[str(n)]
    else:
        for prime in list_primes:
            if n%prime == 0:
                return [prime] + get_factors(n//prime, f)
                break

def all_factors(N):
    factors = dict((str(x), [x]) for x in list_primes)
    for num in range(2, N):
        if str(num) not in factors:
            factors[str(num)] = get_factors(num, factors)
    return factors

N = 1000000
list_primes = primes(N)
list_factors = all_factors(N)
list_unpacked = list(sorted([(int(x), len(set(y))) for x, y in list_factors.items()]))
list_nfactors = "".join([str(y) for x, y in list_unpacked])

list_unpacked[search("4444", list_nfactors).start():(search("4444", list_nfactors).start()+4)][0][0]