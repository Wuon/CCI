# ATTEMPT ONE
# 
# Time Complexity: O(n)
#
# I am assuming that the string contains ONLY characters from the alphabet.
# I can easily accomadate more characters by expanding the ASCII range.
# Looking at the problem, we can identify three scenarios. string is one longer, 
# one shorter, or no change. If one string is two or more characters longer,
# the conidtions are automatically false. In this solution, I first added then subtracted
# between the strings. This will leave me with two options. If the absolute sum of the list
# for strings with different lengths is 1, the condition holds true. Otherwise if the strings
# are of the same length, then we must compare if the absolute sum is 0 or 2. Any more and
# there is more than one change.  

def oneAway(s1, s2):
    if(len(s1) - len(s2) > 1):
        return False
    store = [0] * 26
    s1 = list(s1)
    s2 = list(s2)
    sum = 0 
    for c in s1:
        store[ord(c)-97] += 1
    for c in s2:
        store[ord(c)-97] -= 1
    for i in store:
        sum += abs(i)
    return sum <= 2 if len(s1) == len(s2) else sum <=1
