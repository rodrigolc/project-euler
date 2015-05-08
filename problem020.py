#!/bin/env python

def fact(n):
	return 1 if n <= 1 else n * fact(n-1)

print sum([int(n) for n in str(fact(100))])