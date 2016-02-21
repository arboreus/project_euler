#39) Integer right triangles
#If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#{20,48,52}, {24,45,51}, {30,40,50}
#For which value of p ≤ 1000, is the number of solutions maximised?

# Solution
from math import sqrt

# We are going to look for Pythagorean triples: a^2 + b^2 = c^2 where a < b < c
# We are going to use Dickson's method: find r,s,t in N where r^2 = 2*s*t, then x=r+s, y=r+t, z=r+s+t
P = 1000
list_r = [r for r in range(1, P//3) if (r**2 / 2) % 1 == 0]
list_rst = [(r, s, int(r**2/2/s)) for r in list_r for s in range(1, int(sqrt(r**2/2))+1) if (r**2/2/s)%1 == 0]
list_abc = [(r+s, r+t, r+s+t) for r,s,t in list_rst if 3*r+2*s+2*t <= P]
list_p = [a+b+c for a,b,c in list_abc]

max(set(list_p), key = list_p.count)