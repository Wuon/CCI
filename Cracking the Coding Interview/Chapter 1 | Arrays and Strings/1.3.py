# ATTEMPT ONE
# 
# Time Complexity: O(n)
#
# Since s, the given string comes with padding for the %20 to fit, and t, the true length
# this question becomes much easier to handle. First we need to be able to mutate the string
# so we have to turn it into a character array. Then by finding out the total length of the
# array (including whitespace), we can iterate from end to start without having to cause
# any unwanted overwriting. We need a variable l to track at what position we must insert
# the next character since moving one space and three spaces are different.

def urlify(s, t):
    s = list(s)
    l = len(s) - 1
    for c in range(t-1,-1,-1):
        if(s[c] == ' '):
            s[l] = '0'
            s[l-1] = '2'
            s[l-2] = '%'
            l -= 3
        else:
            s[l] = s[c]
            l -= 1
    return ''.join(s)
