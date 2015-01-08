#!/bin/env python
import math
num = 600851475143
lim = math.sqrt(num)
prime = 3 # num isn't divisible by 2, so we can skip that.
big_prime = prime
while prime <= lim and num >= prime:
	if num % prime == 0:
		num = num/prime
		big_prime = prime
	else:
		prime += 2 # primes != 2 aren't even

print(big_prime)
		
