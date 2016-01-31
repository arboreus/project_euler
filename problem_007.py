#7) 10001st prime
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

# Solution
def prime(n):
    primes = [2, 3, 5, 7]
    if n < 5:
        yield primes[n-1]
    else:
        candidate = 11
        while len(primes) <= n:
            limit = candidate ** 0.5
            for p in primes:
                if p > limit:
                    primes.append(candidate)
                    break
                if candidate % p == 0:
                    break
            candidate += 2
        yield primes[n-1]
        
list(prime(10001))[0]