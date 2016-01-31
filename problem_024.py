#24) Lexicographic permutations
#A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#012   021   102   120   201   210
#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# Solution
import math

def sub(n, i):
    if n > 0 and i > 0:
        c = 0
        while n > math.factorial(i):
            n -= math.factorial(i)
            c += 1
        return [(n, c*math.factorial(i), c)] + sub(n, i-1)
    else:
        return [(n, 0, 0)]
        
pos = [z for x, y, z in sub(10**6, 9)]

def shift(l):
    string = list(range(10))
    result = []
    for i in l:
        result.append(string[i])
        string.pop(i)
    return "".join([str(x) for x in result])
        
shift(pos)