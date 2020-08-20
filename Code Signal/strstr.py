def strstr(s, x):
    lps = computeLPS(x)
    i = j = 0

    while i < len(s):
        if x[j] == s[i]:
            j += 1
            i += 1
        
        if j == len(x):
            return i-j
        
        if i < len(s) and x[j] != s[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return -1

def computeLPS(x):
    length = 0
    lps = [0] * len(x)
    i = 1

    while i < len(x):
        if x[i] == x[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps
