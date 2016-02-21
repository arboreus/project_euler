#35) Circular primes
#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#How many circular primes are there below one million?

# Solution
from itertools import permutations

def primes(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]
    
def cycles(numstr):
    return set([int((numstr + numstr)[y:y+len(numstr)]) for y in range(0, len(numstr))]) 

list_potential = [x for x in primes(1000000) if x < 6 or len(set(str(x)).intersection('024568')) == 0]
list_circular = [x for x in list_potential if cycles(str(x)).issubset(list_potential)]

len(list_circular)