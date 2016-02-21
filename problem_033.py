#33) Digit cancelling fractions
#The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
#If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

# Solution
from numpy import product
from itertools import permutations

def f(lst):
    return int("".join(lst))

list_fractions = [
("".join(x), f(x[:2])/f(x[1:]), f(x[:1])/f(x[2:]))
for x in permutations('123456789', 3)
if f(x[:2])/f(x[1:]) == f(x[:1])/f(x[2:]) < 1
]

product([int(x[2]) for x, y, z in list_fractions]) / \
product([int(x[0]) for x, y, z in list_fractions])
