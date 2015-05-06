#!/bin/env python

def enunciate(num):
	string = ""
	if num == 1000:
		return "one thousand"
	elif num >= 100:
		string = enunciate(num/100) + " hundred"
		if num % 100 != 0:
			string += " and " + enunciate(num % 100)
	elif num >= 20:
		if num >=90:
			string = "ninety"
		elif num >=80:
			string = "eighty"
		elif num >=70:
			string = "seventy"
		elif num >=60:
			string = "sixty"
		elif num >=50:
			string = "fifty"
		elif num >=40:
			string = "forty"
		elif num >=30:
			string = "thirty"
		elif num >=20:
			string = "twenty"	
		if num % 10:
			string += "-"+enunciate(num%10)
	elif num == 19:
		string = "nineteen"
	elif num == 18:
		string = "eighteen"
	elif num == 17:
		string = "seventeen"
	elif num == 16:
		string = "sixteen"
	elif num == 15:
		string = "fifteen"
	elif num == 14:
		string = "fourteen"
	elif num == 13:
		string = "thirteen"
	elif num == 12:
		string = "twelve"
	elif num == 11:
		string = "eleven"
	elif num == 10:
		string = "ten"
	elif num == 9:
		string = "nine"
	elif num == 8:
		string = "eight"
	elif num == 7:
		string = "seven"
	elif num == 6:
		string = "six"
	elif num == 5:
		string = "five"
	elif num == 4:
		string = "four"
	elif num == 3:
		string = "three"
	elif num == 2:
		string = "two"
	elif num == 1:
		string = "one"
	return string
	
s = 0
for i in range(1,1001):
	s += len( [ k for k in enunciate(i) if k != ' ' and k != '-'])
print s