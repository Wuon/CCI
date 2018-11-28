#!/bin/python3

import sys

s = set()
a, b = 100, 100
while a < 999:
    while b < 999:
        if 101101 < a*b < 1000000:
            if a*b % 1000 == int(str(a*b//1000)[::-1]):
                if a*b not in s:
                    s.add(a*b)
        b += 1
    b = 100
    a += 1

s = sorted(s)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    last = 101101
    for a in sorted(s):
        if a >= n:
            print(last)
            break
        last = a
