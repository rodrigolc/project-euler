#!/bin/env python

number1 = 1
number2 = 2
number3 = 3

sum = 0

while number2 < 4000000:
	sum += number2
	number1 = number2 + number3
	number2 = number3 + number1
	number3 = number1 + number2

print(sum)
