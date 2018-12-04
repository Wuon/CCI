#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    num = str(input().strip())
    max = 0
    for i in range(0, n-k):
        prod = 1
        for c in num[i:i+k]:
            prod *= int(c)
        if prod > max:
            max = prod
    print(max)

