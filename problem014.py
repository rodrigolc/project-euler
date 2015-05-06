#!/bin/env python

def collatz(num):
	counter = 1
	while num != 1:
		num = num/2 if num % 2 == 0 else num*3+1
		counter+=1
	return counter

col = 0
num = 0
for i in range(1,1000000):
	col_ = collatz(i)
	if col_ > col:
		num = i
		col = col_

print num, col
	