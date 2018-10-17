# ATTEMPT ONE
# 
# Time Complexity: O(n)
# 
# Given the two strings, I compare characters
# from s2 to s1 and if they match, compare substrings
# of s2 to s1. Because its a rotation, when we slice
# the occurence of the character forward and backwards
# and combine them, we can check to see if the new string
# matches.

def rotateString(s1, s2):
    if(len(s1) != len(s2)):
        return False
    for i in range(0, len(s2)):
        if s2[i] == s1[0]:
            if s1 == s2[i:] + s2[:i]:
                return True
            else:
                break
    return False