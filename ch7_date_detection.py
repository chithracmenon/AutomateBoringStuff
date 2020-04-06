"""Date Detection
Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999. Note that if the day or month is a single digit, it’ll have a leading zero.

The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept nonexistent dates like 31/02/2020 or 31/04/2021. Then store these strings into variables named month, day, and year, and write additional code that can detect if it is a valid date. April, June, September, and November have 30 days, February has 28 days, and the rest of the months have 31 days. February has 29 days in leap years. Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400. Note how this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date."""

#!python3
# Date Detection 


import regex as re
import sys
regexobject = re.compile(r'([0-2]?[0-9]|31|30)/([0]?[0-9]|[1][0-2])/([1-2][0-9][0-9][0-9])')

date = '29/2/2020'

mo = regexobject.findall(date)
if len(mo):
	date = int(mo[0][0])
	month = int(mo[0][1])
	year = int(mo[0][2])
else:
	print("Not valid date")
	sys.exit()

def leap_year(year):
	return  (~(year % 4) and (year % 100) or ~(year % 400)))


months_with30 = [4, 6, 9, 11]

if (month in months_with30) and (date <= 30):
	print("Valid date1")
elif (month == 2) and ((date <= 28) or ((date <= 29) and (leap_year(year)))):
	print("valid date2")
elif (month not in (months_with30 + [2])) and (date <= 31):
	print("valid date4")
else:
	print("invalid date")



print(date, month, year)



