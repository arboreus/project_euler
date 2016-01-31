#25) 1000-digit Fibonacci number
#The Fibonacci sequence is defined by the recurrence relation: Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#The 12th term, F12, is the first term to contain three digits.
#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

# Solution
def d_fibonacci(n): # Djiksta's algorithm
    if n == 0 or n == 1:
        return n
    elif n%2 == 1:
        return d_fibonacci(n//2)**2 + d_fibonacci(n//2+1)**2
    else:
        return d_fibonacci(n//2)*(2*d_fibonacci(n//2-1) + d_fibonacci(n//2))
        
list_1000 = [(x, len(str(d_fibonacci(x)))) for x in list(range(0, 10001, 1000))]
list_100 = [(x, len(str(d_fibonacci(x)))) for x in list(range(4000, 5001, 100))]
list_10 = [(x, len(str(d_fibonacci(x)))) for x in list(range(4700, 4801, 10))]
list_1 = [(x, len(str(d_fibonacci(x)))) for x in list(range(4780, 4791, 1))]