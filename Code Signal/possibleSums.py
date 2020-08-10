def possibleSums(coins, quantity):
    s = {0}
    for i in range(len(coins)):
        coin = coins[i]
        newS = set()
        for result in s:
            for counter in range(quantity[i]):
                newS.add(result + coin * (counter + 1))
        s |= newS
    return len(s) - 1
