#!/bin/python3

import sys

s = set()
p = []
s.add(1)
for i in range(2, 104730):
    if i not in s:
        p.append(i)
        n = i
        while n+i < 104730:
            n += i
            s.add(n)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(p[n-1])
