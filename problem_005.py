#5) Smallest multiple
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Solution
def decompose(lst):
    if lst and lst != [1]:
        ls = [x for x in lst if x != 1]
        elem = ls[0]
        l = [x // elem if x % elem == 0 else x for x in ls]
        return [elem] + decompose(l)
    else:
        return []

def prod(x):
    product = 1
    for i in x:
        product *= i
    return product

prod(decompose(list(range(1, 21))))