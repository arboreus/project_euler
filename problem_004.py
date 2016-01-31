#4) Largest palindrome product
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

# Solution
def if_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

def palindromes(n):
    nums = []
    for i in range(10**(n-1), 10**n):
        for j in range(i, 10**n):
            if i*j not in nums and if_palindrome(i*j):
                nums.append(i*j)
    return nums

max(palindromes(3))