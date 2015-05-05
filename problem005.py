#!/bin/env python

def small_factoring(num):
	aux = []
	i = 2
	while num > 1:
		if num % i == 0:
			num = num//i
			aux.append(i)
		else:
			i += 1
	return aux

def lcm(number,divisor):
	divs = small_factoring(divisor)
	aux = number
	for div in divs:
		if aux % div == 0:
			aux = aux // div
		else:
			number *= div
	return number

num = 1

for div in range(0,21): #21 cause 20 would take us until 19
	num = lcm(num,div)

print (num)
