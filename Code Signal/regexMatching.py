def regexMatching(pattern, test):
    if not pattern:
        return test
    if pattern[0] == '^':
        for i in range(1, len(pattern)):
            if pattern[i] != test[i - 1]:
                return False
    elif pattern[-1] == '$':
        for i in range(1, len(pattern)):
            if pattern[-i - 1] != test[-i]:
                return False
    else:
        return pattern in test
    return True
