#17) Number letter counts
#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

# Solution
digits = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
decades = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def spell(n):
    if n < 10:
        return digits[n]
    elif n < 20:
        return teens[n-10]
    elif n < 100:
        return decades[n//10] + "-" + spell(n%10)
    elif n < 1000:
        if n%100 == 0:
            return spell(n//100) + " hundred"
        else:
            return spell(n//100) + " hundred and " + spell(n%100)
    elif n < 1000000:
        return spell(n//1000) + " thousand " + spell(n%1000)
        
words = [spell(x) for x in list(range(1, 1001))]
len(''.join(words).replace('-', '').replace(' ', ''))