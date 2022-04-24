#49) Prime permutations
#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
#(i) each of the three terms are prime, and,
#(ii) each of the 4-digit numbers are permutations of one another.
#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
#What 12-digit number do you form by concatenating the three terms in this sequence?

#%% Solution
from itertools import permutations

def primes(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]

def perm(n):
    return [int("".join(x)) for x in permutations(str(n))]

list_primes = [x for x in primes(10000) if x > 1000]
list_first = [x for x in list_primes if x+3330 in list_primes and x+6660 in list_primes]
list_first = [x for x in list_first if x+3330 in perm(x) and x+6660 in perm(x)]

int(str(list_first[1]) + str(list_first[1]+3330) + str(list_first[1]+6660))
