#22) Names scores
#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#What is the total of all the name scores in the file?

# Solution
import string

with open(".../p022_names.txt", mode='r') as doc:
    names = doc.read().replace('"', '').split(',')
    
def score(name):
    return sum([string.ascii_uppercase.index(l)+1 for l in name])

names_sorted = sorted(names)
names_scores = [score(x)*(names_sorted.index(x)+1) for x in names_sorted]

sum(names_scores)