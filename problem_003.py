#3) Largest prime factor
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

# Solution
def primes_naive(n):
    if n < 2: return []
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def primes(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]
      
def prod(x):
    product = 1
    for i in x:
        product *= i
    return product
    
def prime_factors(n, m):
    nums = [x for x in primes(m) if n % x == 0]
    if prod(nums) == n:
        return nums
    else:
        return []

max(prime_factors(600851475143, 10000))  