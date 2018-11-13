# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
# multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

# !/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    three = (n - 1) // 3
    five = (n - 1) // 5
    fifteen = (n - 1) // 15
    print(((3 * three * (three + 1)) >> 1) + ((5 * five * (five + 1)) >> 1) - ((15 * fifteen * (fifteen + 1)) >> 1))
