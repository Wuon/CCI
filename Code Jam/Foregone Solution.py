t = int(input())
for _ in range(t):
    x = input()
    a = list(x)
    b = list(x)
    for i in range(len(x)):
        if x[i] == '4':
            a[i] = '3'
            b[i] = '1'
        else:
            b[i] = '0'
    print("Case #" + str(_+1) + ": " + str(int("".join(a), 10)) + " " + str(int("".join(b), 10)))
