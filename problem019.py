#!/bin/env python

day_month = [31,28,31,30,31,30,31,31,30,31,30,31]

def leap_year(year):
	return year%4 == 0 and year %100 != 0
def days_from_start(day,month,year): #start = d=0,m=1,y=1900
	d_years = year - 1900 #will never be negative
	days_total = (d_years - 1)/4 
	if year > 2000: #correct for y2k
		days_total -= 1
	days_total += d_years * 365
	days_total += sum(day_month[0:month])
	if month > 2 and leap_year(year):
		days_total += 1
	days_total += day
	return days_total 

def day_of_week(day,month,year):
	return days_from_start(day,month,year) % 7

sundays = 0
for y in range(1901,2001):
	for m in range(1,13):
		 if day_of_week(1,m,y) == 0:
			 sundays += 1

print sundays
	