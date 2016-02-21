#36) Double-base palindromes
#The decimal number, 585 = 1001001001|2 (binary), is palindromic in both bases.
#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#(Please note that the palindromic number, in either base, may not include leading zeros.)

# Solution
def is_palindrome(x):
    return "".join(reversed(x)) == x and x[0] != "0"

list_potential = [x for x in range(1000000) if is_palindrome(str(x))]
list_palindromes = [x for x in list_potential if is_palindrome(bin(x)[2:])]

sum(list_palindromes)