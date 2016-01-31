#13) Large sum
#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

nums = """
37107287533902102798797998220837590246510135740250
...
53503534226472524250874054075591789781264330331690
""".replace('\n', ' ').strip().split(' ')

# Solution
str(sum([int(x) for x in nums]))[:10]
