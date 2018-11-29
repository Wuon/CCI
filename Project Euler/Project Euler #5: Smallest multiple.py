#!/bin/python3
import math
import sys

s = set()
s.add(1)
for i in range(2, 40):
    if i not in s:
        n = i
        while n+i < 40:
            n += i
            s.add(n)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum = 1
    for i in range(1, n+1):
        if i not in s:
            sum *= i ** math.floor(math.log(n) / math.log(i))
    print(sum)
