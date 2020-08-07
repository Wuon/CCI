def firstDuplicate(a):
    seenNumbers = set()
    for number in a:
        if number in seenNumbers:
            return number
        else:
            seenNumbers.add(number)
    return -1
