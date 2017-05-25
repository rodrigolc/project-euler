#!/bin/env python

import math

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 1000000 - 1
while len(nums) > 0:
    fac = math.factorial(len(nums) - 1)

    print(nums[target / fac], fac, target)
    nums.pop(target / fac)
    target -= fac * (target / fac)
