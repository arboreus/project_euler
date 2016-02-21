#31) Coin sums
#In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#It is possible to make £2 in the following way:
#1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#How many different ways can £2 be made using any number of coins?

# Solution
from numpy import array, dot

# c200 can only be used once, c1 is used to reach 200 from any value < 200
coins = array([100, 50, 20, 10, 5, 2]) 
stacks = [
array([c100, c50, c20, c10, c5, c2])
for c100 in range(3)
for c50 in range(5)
for c20 in range(11)
for c10 in range(21)
for c5 in range(41)
for c2 in range(101)
if dot(array([c100, c50, c20, c10, c5, c2]), coins) <= 200
]

len(stacks)+1