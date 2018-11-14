#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    lp = 0
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            lp = n
            n /= i
        i += 1
        if n > 1:
            lp = n
    print(int(lp))
