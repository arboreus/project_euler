#32) Pandigital products
#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

# Solution
from itertools import permutations

def f(lst):
    return int("".join(lst))

list_equations = [
(f(x[:y]), f(x[y:5]), f(x[5:])) 
for x in permutations('123456789') 
for y in range(1, 3)
if f(x[:y]) * f(x[y:5]) == f(x[5:])
]

sum(set([z for x, y, z in list_equations]))