def meanGroups(a):
    d = {}
    for i in range(len(a)):
        group = a[i]
        mean = sum(group) / len(group)
        if mean not in d:
            d[mean] = []
        d[mean].append(i)
    output = []
    for item in d:
        output.append(d[item])
    return output
