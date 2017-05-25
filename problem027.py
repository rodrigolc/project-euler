#!/bin/env python
import math


def prime(num):  		# version from previous c++ implementation by yours truly
                        # from original code: "// THIS IS MAGIC, GUYS! FAST AS HELL."
                        # oh, younger me.
    if num < 2:
        return False
    elif num % 2 == 0 and num != 2:
        return False
    for i in range(3, int(math.ceil(math.sqrt(num))) + 1, 2):
        if num % i == 0:
            return False
    return True


cand = 0


def seq(a, b):
    global cand
    n = 0
    while prime(n**2 + n * a + b):
        n += 1
    if n > cand:
        print a, b, n, a * b
        cand = n
    return n


total = [ (A, B, seq(A, B)) for A in range(-999, 1000, 1)
          for B in range(-1000, 1001, 1)]
print cand