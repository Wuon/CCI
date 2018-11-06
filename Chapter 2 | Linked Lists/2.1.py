# ATTEMPT ONE
# 
# Time Complexity: O(n) ****** Your current code is O(N^2) runtime
#
# For this question, I used a storage list to keep
# track off the unique occurrences of objects and
# as we iterate through the linked list, check to
# see if there is a match and if there is, switch
# the previous nodes next pointer to the next of the 
# current.


'''
Use hashset - then it will be O(N) because searching through s will be constant time

E.G

s = set()
if current.get_data() not in s:
    s.add(current.get_data())


You're Welcome - Zi
'''


def remove_duplicates(l):
    s = []
    current = l.head
    previous = None
    while current is not None:
        if current.get_data() not in s:
            s.append(current.get_data())
            previous = current
        else:
            l.delete(previous)
        current = current.get_next()
