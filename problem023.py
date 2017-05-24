#!/bin/env python

def checa_abund(x):
	print(x)
	return True if sum([y for y in range(1,x/2 + 1) if x%y == 0]) > x else False

abundantes = [y for y in range(1,28123) if checa_abund(y)]
print("oi")
hot_pot = set([x+y for x in abundantes for y in abundantes if x + y < 28123])
print(hot_pot)
print(sum([x for x in range(1,28123) if x not in hot_pot]))
