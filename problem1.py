#!/bin/env python

#three's
m3s = [ x for x in range(0,1000,3)]

#five's not %3
m5s = [ x for x in range(0,1000,5) if not x%3 == 0]

print( sum(m3s) + sum(m5s))
