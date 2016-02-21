#38) Pandigital multiples
#Take the number 192 and multiply it by each of 1, 2, and 3:
#192 × 1 = 192
#192 × 2 = 384
#192 × 3 = 576
#By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
#The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

# Solution
def pan_product(x):
    digits = ""
    n = 1
    while len(digits) < 9:
        digits = digits + str(x*n)
        n = n + 1
    return digits
    
def is_pandigital(numstr):
    return sorted(numstr) == list('123456789')[:len(numstr)]

list_candidates = [x for x in range(10000) if str(x)[0] == '9']
list_multipliers = [x for x in list_candidates if is_pandigital(pan_product(x))]

max([pan_product(x) for x in list_multipliers])