for a0 in range(int(input().strip())):
    n = map(int, str(2 ** int(input().strip())))
    tot = 0
    for digit in n:
        tot += digit
    print(tot)
