# ATTEMPT ONE
# 
# Time Complexity: O(n)
#
# For this question, I used a storage list to keep
# track off the unique occcurences of objects and
# as we iterate through the linked list, check to
# see if there is a match and if there is, switch
# the previous nodes next pointer to the next of the 
# current.

from SinglyLinkedList import LinkedList

def removeDuplicates(l):
    s = []
    current = l.head
    previous = None
    while current != None :
        if current.get_data() not in s:
            s.append(current.get_data())
            previous = current
        else:
            l.delete(previous)
        current = current.get_next()
        