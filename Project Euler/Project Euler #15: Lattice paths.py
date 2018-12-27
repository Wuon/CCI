import math

for a0 in range(int(input().strip())):
    n = input().split(' ')
    print(math.factorial(int(n[0]) + int(n[1]))//(math.factorial(int(n[0])) * math.factorial(int(n[1]))) % 1000000007)
