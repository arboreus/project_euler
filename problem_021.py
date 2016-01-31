#21) Amicable numbers
#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#Evaluate the sum of all the amicable numbers under 10000.

#import math
#def fac(n):
#    step = lambda x: 1 + x*4 - x//2*2
#    maxq = math.floor(math.sqrt(n))
#    d = 1
#    q = n % 2 == 0 and 2 or 3 
#    while q <= maxq and n % q != 0:
#        q = step(d)
#        d += 1
#    return q <= maxq and [q] + fac(n//q) or [n]

# Solution
def div(n):
    return [x for x in range(1, n) if n%x==0]
    
def amic(m, n):
    return True if sum(div(m))==n and sum(div(n))==m else False
    
A = [(x,sum(div(x)), sum(div(sum(div(x))))) for x in range(1, 10000)]
B = list(set([(min(x), max(x)) for x in A if x[0]==x[2] and x[0]!=x[1]]))

sum([sum(x) for x in B])