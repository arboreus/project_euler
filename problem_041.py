#41) Pandigital prime
#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#What is the largest n-digit pandigital prime that exists?

#%% Solution
def is_pandigital(x):
    return sorted(str(x)) == list('123456789')[:len(str(x))]

def primes(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]


list_primes = primes(10**9)
list_pandigital_primes = [x for x in list_primes if is_pandigital(x)]

max(list_pandigital_primes)
