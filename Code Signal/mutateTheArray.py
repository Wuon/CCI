def mutateTheArray(n, a):
    padded = [0] + a + [0]
    output = []
    for i in range(1, len(padded) - 1):
        output.append(padded[i] + padded[i-1] + padded[i+1])
    return output
