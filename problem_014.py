#14) Longest Collatz sequence
#The following iterative sequence is defined for the set of positive integers:
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)
#Using the rule above and starting with 13, we generate the following sequence: 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#Which starting number, under one million, produces the longest chain?
#NOTE: Once the chain starts the terms are allowed to go above one million.

# Solution
def collatz(n):
    nums = []
    while n > 1:
        nums.append(n)
        n=(n//2,n*3+1)[int(n%2)]
    return nums+[1]
    
def collatz_count(n, d = {1: 1}):
    stack = []
    while n not in d:
        stack.append(n)
        n = n * 3 + 1 if n & 1 else n // 2
    c = d[n]
    while stack:
        c += 1
        d[stack.pop()] = c
    return c

counts = [(x, collatz_count(x)) for x in range(1, 10**6)]
sorted(counts, key=lambda tup: tup[1], reverse = True)[0]