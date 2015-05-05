#!/bin/env python3
import math


def prime(num): #version from previous c++ implementation by yours truly
				#from original code: "// THIS IS MAGIC, GUYS! FAST AS HELL."
				#oh, younger me.
	if num % 2 == 0:
		return False
	for i in range(3,int(math.ceil(math.sqrt(num))) + 1,2):
		if num % i == 0:
			return False
	return True

psum = 2
number = 3 # would start with 3, but will inc by 2 each iteraction
while number < 2000000:
	if prime(number):
		psum += number
	number += 2
print(psum)