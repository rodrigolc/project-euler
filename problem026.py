#!/bin/env python


def gen_cycle(start, denom):
    checks = set()
    while True:
        while start < denom:
            start *= 10
            yield 0
        if start in checks:
            break
        else:
            yield start/denom
            checks.add(start)
            start = (start % denom) * 10

def find_cycle(denom):
    checks = set()
    start = 1
    while True:
        while start < denom:
            start *= 10
        if start in checks:
            return gen_cycle(start, denom)
        else:
            checks.add(start)
            start = (start % denom)
            if start == 0:
                return []

results = [(x,len(list(find_cycle(x)))) for x in range(2,1001)]
results.sort(cmp=lambda x, y:y[1] - x[1])
print results[0][0]