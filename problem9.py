#!/bin/env python3
import math

for a in range(1,250):
	for b in range(a,500):
		c = 1000 - a - b
		if a*a + b*b == c*c:
			print(a,b,c,a*b*c)

