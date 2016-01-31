#23) Non-abundant sums
#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

# Solution
import itertools

def div(n):
    if n == 1: return [1]
    return [x for x in range(1, n) if n%x==0]

nums_all = [(x, div(x)) for x in range(1, 28124)]
nums_abundant = [x for x, y in nums_all if sum(y) > x]
nums_sum2 = list(set([sum(x) for x in itertools.combinations(nums_abundant, 2) if sum(x) < 28124] + [x*2 for x in nums_abundant]))
nums_result = [x for x in range(1, 28124) if x not in nums_sum2]

sum(nums_result)