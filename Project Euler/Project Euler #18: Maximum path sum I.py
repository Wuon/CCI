for x in range(int(input().strip())):
    data = []
    for y in range(int(input().strip())):
        data.append(list(map(int, input().split(' '))))
    for i in range(len(data)-1, 0, -1):
        for j in range(0, i):
            num = data[i-1][j] + data[i][j]
            num2 = data[i-1][j] + data[i][j+1]
            data[i-1][j] = num if num > num2 else num2
    print(data[0][0])

