#26) Reciprocal cycles
#A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#1/2	= 	0.5
#1/3	= 	0.(3)
#1/4	= 	0.25
#1/5	= 	0.2
#1/6	= 	0.1(6)
#1/7	= 	0.(142857)
#1/8	= 	0.125
#1/9	= 	0.(1)
#1/10	= 	0.1
#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

# Solution
from decimal import Decimal, getcontext
getcontext().prec = 2000

# If 1/m is a repeating decimal and 1/n is a terminating decimal, them 1/(mn) has a nonperiodic part 
# whose length is that of 1/n and a repeating part whose length is that of 1/m.
denoms_terminating = [x*y for x in [2**x for x in range(10)] for y in [5**x for x in range(5)]]
denoms_terminating = [x for x in sorted(list(set(denoms_terminating))) if 1 < x < 1000]

for number in reversed(denoms_terminating):
    denoms = [x for x in range(2, 1000)]
    denoms = [x // number if x % number == 0 else x for x in denoms]
    denoms = [x for x in sorted(list(set(denoms))) if x > 1]

def sequence_length(seq):
    for x in range(1, len(seq) // 2 + 1):
        chunks = [seq[i:i+x] for i in range(0, len(seq), x)]
        if len(set(chunks)) == 1:
            return x
    return 0

decimals = [(x, str(Decimal(1) / Decimal(x))[2:(2+(x-1)*2)]) for x in denoms]
periods = [(x, sequence_length(y)) for x, y in decimals]

[x for x, y in periods if y == max([y for x, y in periods])][0]