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


def find_factors(num):
    factors = 1
    for current in p:
        count = 1
        if current > num:
            break
        while num % current == 0:
            num /= current
            count += 1
        factors *= count
    return factors


def triangle_number(num):
    return int(num * (num+1) / 2)


store = []
d = 0
t = 1

while d < 1000:
    factor = find_factors(triangle_number(t))
    if factor > d:
        while len(store) < factor:
            store.append(triangle_number(t))
        d = factor
    t += 1

for a0 in range(int(input().strip())):
    n = int(input().strip())
    print(store[n])
