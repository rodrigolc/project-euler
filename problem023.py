#!/bin/env python3


def checa_abund(x):
    print(x)
    return True if (sum([y for y in range(1, x / 2 + 1) if x % y == 0]) > x) else False


abundantes = [ab for ab in range(1, 28123) if checa_abund(ab)]
print("oi")
hot_pot = set([a + b for a in abundantes for b in abundantes if a + b < 28123])
print(hot_pot)
print(sum([nab for nab in range(1, 28123) if nab not in hot_pot]))
