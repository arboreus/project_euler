#27) Quadratic primes
#Euler discovered the remarkable quadratic formula: n^2 + n + 41
#It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. 
#However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
#The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.
#Considering quadratics of the form: n^2 + an + b, where |a| < 1000 and |b| < 1000
#where |n| is the modulus/absolute value of n (e.g. |11| = 11 and |−4| = 4)
#Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

# Solution
def primes(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]
    
def f(a, b, n): 
    return n**2+a*n+b
   
def is_prime(a, b, n):
    return f(a, b, n) in primes(f(a, b, n)+1)
    
list_candidates = [(x, y) for x in range(-999, 1000) for y in primes(1000)]

for n in range(40):
    list_candidates = [(x, y) for x, y in list_candidates if f(x, y, n) > 1]
   
n = 1
while len(list_candidates) > 1:
    list_candidates = [(x, y) for x, y in list_candidates if is_prime(x, y, n)]
    n = n + 1

list_candidates[0][0] * list_candidates[0][1]