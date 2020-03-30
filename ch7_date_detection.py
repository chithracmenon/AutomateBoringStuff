#! ch_7_date_detection.py

import regex as re
import sys
regexobject = re.compile(r'([0-2]?[0-9]|31|30)/([0]?[0-9]|[1][0-2])/([1-2][0-9][0-9][0-9])')

print("Input a date")
date = input()

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
	print("Invalid date")





