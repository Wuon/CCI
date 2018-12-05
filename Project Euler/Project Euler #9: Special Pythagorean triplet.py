#!/bin/python3
import math
import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    val = 0
    for a in range(1, n):
        b = (n * (n-2*a))/(2 * (n - a))
        if b % 1 == 0:
            c = n - a - b
            if a ** 2 + b ** 2 == c ** 2 and a + b + c == n:
                val = a * b * c if (a * b * c > val) else val
    print(-1 if val == 0 else int(val))
