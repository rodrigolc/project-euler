#!/bin/env python3

sum_squares = sum([x**2 for x in range(1, 100 + 1)])
square_sum = sum([x for x in range(1, 100 + 1)]) ** 2

difference = sum_squares - square_sum
print(difference)
