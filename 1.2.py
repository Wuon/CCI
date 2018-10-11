# ATTEMPT ONE
# 
# I am assuming that the string contains ONLY characters from the alphabet.
# I can easily accomadate more characters by expanding the ASCII range.
# The thought process I had while designing this algorithm was to create an integer array
# storing the occurence of characters in the first string. Then by removing the occurence in 
# the second string, if any of the elements go below 0, then s1 and s2 are not permutations.
# Another thing to note is that if s1 and s2 are not the same size, we can assume they are 
# not permutations.

def check(s1,s2):
    store = [0] * 26
    if(len(s1) != len(s2)):
        return False
    for c in b:
        store[ord(c)-97]+=1
    for c in s:
        store[ord(c)-97]-=1
        if(store[ord(c)-97] < 0):
            return False
    return True
