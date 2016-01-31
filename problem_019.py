#19) Counting Sundays
#You are given the following information, but you may prefer to do some research for yourself.
#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# Solution
import datetime

limits = [datetime.date(1901, 1, 1), datetime.date(2000, 12, 31)]
dates = [limits[0] + datetime.timedelta(days=x) for x in range(0, (limits[1] - limits[0]).days + 1)]
first = [x for x in dates if x.day == 1]
sundays = [x for x in first if x.weekday() == 6]

len(sundays)