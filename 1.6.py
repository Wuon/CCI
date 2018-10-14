# ATTEMPT ONE
# 
# Time Complexity: O(n)
#
# In this algorithm, we only have to iterate through the string once.
# This is done by comparing the next character with the current character.
# If its the same character, increase the occurence, otherwise append to the
# list the character and number. Then return the shorter string.

def stringCompression(s):
    n = []
    o = 0
    for i in range(0, len(s)):
        o += 1
        if i == len(s) - 1 or s[i] != s[i+1]:
            n.extend([s[i],str(o)])
            o = 0
    return s if len(n) >= len(s) else ''.join(n)