def containsCloseNums(nums, k):
    d = {}
    lastSeen = {}
    for index, num in enumerate(nums):
        if num not in d:
            d[num] = 0
            lastSeen[num] = index
        else:
            diff = index - lastSeen[num]
            d[num] += diff
            if d[num] <= k or diff <= k:
                return True
            lastSeen[num] = index
    return False
