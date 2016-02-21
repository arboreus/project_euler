#40) Champernowne's constant
#An irrational decimal fraction is created by concatenating the positive integers:
#0.12345678910 1 112131415161718192021...
#It can be seen that the 12th digit of the fractional part is 1.
#If dn represents the nth digit of the fractional part, find the value of the following expression.
#d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

# Solution
def gen_frac(size):
    frac = ""
    n = 1
    while len(frac) < size:
        frac = frac + str(n)
        n = n + 1
    return frac
    
def prod(x):
    product = 1
    for i in x:
        product *= i
    return product

list_digits = [int(x) for x in gen_frac(1000000)]

prod([list_digits[10**x-1] for x in range(7)])