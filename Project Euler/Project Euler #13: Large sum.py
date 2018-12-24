a = [0] * 50
for a0 in range(int(input().strip())):
    n = input().strip()
    for i in range(0, len(a)):
        cur = int(n[49-i]) if i <= 49 else 0
        if a[i] + cur > 9:
            if i == len(a) - 1:
                a.append((a[i] + cur) // 10)
            else:
                a[i+1] += (a[i] + cur) // 10
            a[i] = (a[i] + cur) % 10
        else:
            a[i] += cur
print(''.join(map(str, a))[-10:][::-1])