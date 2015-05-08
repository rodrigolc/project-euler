#!/bin/env python

f = open("assets/problem067/triangle.txt",'r')
triangle_text = f.read()
f.close()

triangle = [[int(n) for n in s.split(" ")] for s in triangle_text.split("\n")]



for i in range(len(triangle)-2,-1,-1):
	print i
	for j in range(len(triangle[i])):	
		triangle[i][j] += max(triangle[i+1][j],triangle[i+1][j+1])

print triangle[0][0]
