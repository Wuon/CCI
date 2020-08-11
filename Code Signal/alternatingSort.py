def alternatingSort(a):
    new = []
    for i in range(0, len(a) // 2):
        new.append(a[i])
        new.append(a[-(i+1)])
    if len(a) % 2 == 1:
        new.append(a[len(a) // 2])
    prev = new[0]
    for i in range(1, len(new)):
        if new[i] <= prev:
            return False
        prev = new[i]
    return True
