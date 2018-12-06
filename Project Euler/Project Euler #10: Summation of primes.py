#!/bin/python3

import sys

s = set()
t = [0]
s.add(1)
for i in range(2, 1000000):
    if i not in s:
        t.append(i + t[len(t) - 1])
        n = i
        while n+i < 1000000:
            n += i
            s.add(n)
    else:
        t.append(t[len(t) - 1])
x = int(input().strip())
for a0 in range(x):
    n = int(input().strip())
    print(t[n-1])
