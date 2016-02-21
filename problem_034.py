#34) Digit factorials
#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#Note: as 1! = 1 and 2! = 2 are not sums they are not included.

# Solution
from math import factorial
from itertools import permutations, product

def f(lst):
    return sum([factorial(x) for x in lst])

def g(lst):
    return int("".join([str(x) for x in lst]))

list_permutations = [
f(x)
for y in range(2, 7)
for x in product(range(10), repeat=y)
if f(x) == g(x) and x[0] != 0
]

sum(list_permutations)