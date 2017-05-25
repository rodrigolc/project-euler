#!/bin/env python

def dec(num):
    while num > 0:
        yield num % 10
        num /= 10
soma = 0
for i in range(2,354295):
    if i == sum([x**5 for x in dec(i)]):
        soma += i
        print i, list(dec(i))
print soma