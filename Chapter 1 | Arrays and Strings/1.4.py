# ATTEMPT ONE
# 
# Time Complexity: O(n)
#
# To simplify the work done, lets first analyze the requirements for a palindrome.
# The nature of palindrome consists of even pairs of characters with the exeption of
# one odd number character (will always be the center). Folllowing this pattern, 
# we can assume that if there are more than two occurences of odd number characters,
# then the given arrangement cannot form a palindrome.

def pp(s):
    store = [0] * 26
    s = list(s.replace(" ", ""))
    l = 0
    for c in s:
        store[ord(c)-97] += 1
        l += 1 if store[ord(c)-97] % 2 != 0 else -1
    return l <= 1