#37) Truncatable primes
#The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

# Solution
def primes(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]
    
def truncs(numstr):
    return set([int(elem) for tup in [(numstr[:x], numstr[x:]) for x in range(len(numstr))] for elem in tup if elem != ''])

list_potential = [x for x in primes(1000000) if len(set(str(x)[1:]).intersection('024568')) == 0]
list_truncatable = [x for x in list_potential if truncs(str(x)).issubset(list_potential) if x > 7]

sum(list_truncatable)