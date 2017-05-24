#!/bin/env python

d = 1
a = 0
b = 1
c = 1
while d <= 1000:
    b = a+b
    a = b-a
    c += 1
    if b >= 10**d:
        d += 1
        if d == 1000:
            break

print (c)

