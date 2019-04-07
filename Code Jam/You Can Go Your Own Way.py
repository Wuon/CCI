t = int(input())
for _ in range(t):
    l = input()
    x = input()
    y = ""
    for c in x:
        if c == "S":
            y += "E"
        else:
            y += "S"
    print("Case #" + str(_+1) + ": " + y)
