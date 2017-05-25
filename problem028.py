#!/bin/env python

soma = 1
n = 1
inc = 2
while n < 1001*1001:
    n += inc
    soma += n
    n += inc
    soma += n
    n += inc
    soma += n
    n += inc
    soma += n
    inc += 2
print soma, n, 1001*1001