#15) Lattice paths
#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?

# Solution
import math

def npermutations(n, k):
    return math.factorial(n)//(math.factorial(k)*math.factorial(n-k))
    
npermutations(40, 20)