#30) Digit fifth powers
#Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#1634 = 1^4 + 6^4 + 3^4 + 4^4
#8208 = 8^4 + 2^4 + 0^4 + 8^4
#9474 = 9^4 + 4^4 + 7^4 + 4^4
#As 1 = 1^4 is not a sum it is not included.
#The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# Solution
def powers_sum(lst, n):
    return sum([int(x)**n for x in lst])

list_pairs = [(x, powers_sum(str(x), 5)) for x in [x for x in range(100000)]]
list_pairs = [x for x ,y in list_pairs if x == y and x > 9]

sum(list_pairs)
