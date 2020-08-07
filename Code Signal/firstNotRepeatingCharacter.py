def firstNotRepeatingCharacter(s):
    frequency = {}
    firstSeen = {}
    for index, letter in enumerate(s):
        if letter not in frequency:
            frequency[letter] = 0
            firstSeen[letter] = index
        frequency[letter] += 1
    lowest = float('inf')
    for letter in frequency:
        if frequency[letter] == 1:
            lowest = min(lowest, firstSeen[letter])
    return '_' if lowest == float('inf')  else s[lowest]
