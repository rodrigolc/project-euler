#!/bin/env python

def split_digits(num):
	arr = []
	if num == 0:
		return [0]
	while num > 0:
		arr.append(num % 10)
		num = num // 10
	return arr[::-1]

def palindrome(num):
	arr = split_digits(num)
	arr_rev = arr[::-1]
	for i in range(len(arr)):
		if not arr[i] == arr_rev[i]:
			return False
	return True

big_palindrome = 0

for i in range(100,1000):
	for j in range(i,1000):
		if i*j > big_palindrome and palindrome(i*j):
			big_palindrome = i*j

print(big_palindrome)
