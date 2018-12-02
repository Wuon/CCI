#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER_ARRAY wallPoints
#  3. INTEGER_ARRAY lengths
#


def solve(h, wallPoints, lengths):
    min = 0
    for i in range(0, len(wallPoints)):
        cur = math.ceil(wallPoints[i] - lengths[i] * 0.25) - h
        if cur > min:
            min = cur
    return 0 if (min < 0) else min

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    h = int(first_multiple_input[1])

    wallPoints = list(map(int, input().rstrip().split()))

    lengths = list(map(int, input().rstrip().split()))

    answer = solve(h, wallPoints, lengths)

    #fptr.write(str(answer) + '\n')

    #fptr.close()
