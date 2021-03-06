#!/bin/env python3

primes = []

def prime(num): #should be called in order. eg calling (25) before
		## (5) will break it
	for prime in primes:
		if num == prime:
			return True
		elif num % prime == 0:
			return False
	primes.append(num)
	return True

counter = 1 #account for 2
number = 1 # would start with 3, but will inc by 2 each iteraction
prime(2) # get 2 into the prime pool (not that it would change anything)
while counter != 10001:
	number += 2
	if prime(number):
		counter += 1

print(number)

