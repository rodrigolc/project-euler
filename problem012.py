#!/bin/env python

def factor(num):
	facts = {}
	while num % 2 == 0 and num > 1:
		if not 2 in facts:
			facts[2] = 0
		facts[2] += 1
		num /= 2
	counter = 3
	while num > 1:
		while num % counter == 0 and num > 1:
			if not counter in facts:
				facts[counter] = 0
			facts[counter] += 1
			num /= counter
		counter += 2
	return facts

def divisor(num):
	factors = factor(num)
	divs = 1
	for k in factors:
		divs *= factors[k]+1
	return divs

num = 0
counter = 1
while divisor(num) <= 500:
	num += counter
	counter += 1

print num