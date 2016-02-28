#!/bin/env python

import math

def divisor_sum(number):
	limit = int(math.ceil(math.sqrt(number)))
	sum_ = 1
	for i in range(2,limit):
		if number % i == 0:
			sum_ += i
			if (number/i) != i:
				sum_ += (number/i)
	return sum_

sum_ = 0
for i in range(10000):
	x = divisor_sum(i)
	if i == divisor_sum(x) and not x == i:
		sum_ += i
		print i, "==", x
	else:
		print i, "!=", x

print sum_
