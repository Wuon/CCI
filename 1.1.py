# ATTEMPT ONE
# 
# I am assuming that the string contains ONLY characters from the alphabet.
# I can easily accomadate more characters by expanding the ASCII range.
# The thought process I had while designing this algorithm was that since the number
# of characters is known, I could use a hash table to reduce the runtime significantly.
# Rather than doing if c in store (comparing each element would give o(n^2)), using hash
# tables properly reduce the runtime to o(n) as it iterates only once in the for loop for length s.
#
# ATTEMPT TWO
# 
# I realized that if the length of the string exceeds the number of allowed characters,
# the string is guranteed to have a duplicate. By checking to see if the string exceeds the range
# of ASCII characters we are checking for, we can instantly tell without having to do the dirty work.

def isUnique2(s):
    if(len(s) > 26):
        return False
    store = [None] * 26
    for c in s:
        if store[ord(c)-97]:
            return False
        else:
            store[ord(c)-97] = True
    return True