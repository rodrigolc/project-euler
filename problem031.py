#!/bin/env python

coins = [200,100,50,20,10,5,2,1]

soma = 0

def rec(num,coin):
    if num == 0:
        return 1
    elif num < 0:
        return 0
    s = 0
    for i in range(coin,len(coins)):
        s += rec(num-coins[i],i)
    return s


print rec(200,0)
