#45) Triangular, pentagonal, and hexagonal
#Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
#Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
#Pentagonal	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
#Hexagonal	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
#It can be verified that T285 = P165 = H143 = 40755.
#Find the next triangle number that is also pentagonal and hexagonal.

#%% Solution
def tri_penta_hexa(N):
    n = 1
    count = 0
    while count < N:
        x = int(1/2*n*(n+1))
        if (sqrt(24*x+1)+1) % 6 == 0 and (sqrt(8*x+1)+1) % 4 == 0:
            yield x
            count += 1
        n += 1

list(tri_penta_hexa(3))[2]
