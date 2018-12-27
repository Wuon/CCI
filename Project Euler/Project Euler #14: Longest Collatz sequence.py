s = [0] * 5000000
s[0], s[1] = 0, 1
for i in range(2, 5000000):
    steps = []
    cur = i
    while cur < 5000000 and s[cur-1] == 0:
        steps.append(cur)
        cur = (cur >> 1) if (cur % 2 == 0) else (3 * cur + 1)
    if cur > 5000000:
        cur = int((cur-1)/3)
    mark = s[cur-1]
    for j in range(0, len(steps)):
        s[steps[j]-1] = len(steps) - j + mark
for a0 in range(int(input().strip())):
    n = int(input().strip())
    big = 1
    for i in range(1, n):
        big = i if s[i-1] >= s[big-1] else big
    print(big)