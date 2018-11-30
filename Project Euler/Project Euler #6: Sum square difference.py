#!/bin/python3

import sys

s = [1]
for i in range(2, 10001):
    s.append(s[len(s)-1] + i ** 2)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    s1 = 0
    s2 = 0
    for i in range(1, n+1):
        s1 += i
    print((s1 ** 2) - s[n-1])
