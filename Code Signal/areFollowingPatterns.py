def areFollowingPatterns(strings, patterns):
    n = len(patterns)
    split = [strings[i * n:(i + 1) * n] for i in range((len(strings) + n - 1) // n )]  
    for a in split:
        d = {}
        s = set()
        for i in range(len(patterns)):
            if patterns[i] not in d:
                if a[i] in s:
                    return False
                else:
                    s.add(a[i])
                d[patterns[i]] = a[i]
            else:
                if d[patterns[i]] != a[i]:
                    return False
    return True
