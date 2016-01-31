#9) Special Pythagorean triplet
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a^2 + b^2 = c^2.
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

# Solution
def pythagorean_naive(n):
    for a in range(0+1, n):
        for b in range(a+1, n):
            for c in range(b+1, n):
                if a+b+c == n:
                    if a**2 + b**2 == c**2:
                        return [a, b, c]
                    else:
                        continue
                else:
                    continue
    return []

def pythagorean(n):
    for a in range(1, n//3):
        for b in range(a+1, n//2):
            if 2*a*b-2*n*(a+b)+n**2 == 0:
                return [a, b, int((a**2+b**2)**0.5)]
            else:
                continue

def prod(x):
    product = 1
    for i in x:
        product *= i
    return product
    
prod(pythagorean(1000))
