#42) Coded triangle numbers
#The nth term of the sequence of triangle numbers is given by, tn = (1/2)*n*(n+1); so the first ten triangle numbers are:
#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
#Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?


#%% Solution
def triangle_nums(x):
    n = 1
    while int(1/2*n*(n+1)) <= x:
        yield int(1/2*n*(n+1))
        n += 1

with open("p042_words.txt", mode='r') as doc:
    list_words = doc.read().replace('"', '').split(',')
list_values = [sum([ord(x)-64 for x in word]) for word in list_words]
list_triangle = [x for x in list_values if x in triangle_nums(max(list_values))]

len(list_triangle)