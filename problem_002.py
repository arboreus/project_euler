#2) Even Fibonacci numbers
#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# Solution
def fibonacci(n):
    if n > 2:
        return fibonacci(n-2) + fibonacci(n-1)
    else:
        return 1
        
def fibonacci_sequence(n):
    num = 1
    while fibonacci(num) < n:
        yield fibonacci(num)
        num += 1

sum([x for x in fibonacci_sequence(4000000) if x % 2 == 0])