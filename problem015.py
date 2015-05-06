#!/bin/env python

path_map = [[None for j in range(21)] for i in range(21)]

def paths(x,y):
	global path_map
	if path_map[x][y] is not None:
		return path_map[x][y]
	if x == 0 or y == 0:
		path_map[x][y] = 1
	else:
		path_map[x][y] = paths(x-1,y) + paths(x,y-1)
	return path_map[x][y]

print paths(20,20)