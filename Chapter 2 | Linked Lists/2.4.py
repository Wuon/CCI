from SinglyLinkedList import LinkedList


def partition(n, p):
    head = n
    tail = n
    while n is not None:
        if n.get_data() < p:
            n.set_next(head.get_data())
            head = n
        else:
            n.set_next(tail.get_data())
            tail = n
        n = n.get_next()
    tail.set_next(None)

l = LinkedList()
l.insert(3)
l.insert(5)
l.insert(8)
l.insert(5)
l.insert(10)
l.insert(2)
l.insert(1)

partition(l.head, 5)
l.print()
