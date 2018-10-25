from Node import Node


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count
    
    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current
    
    def delete(self, node):
        node.set_next(None if node.get_next().get_next() is None else node.get_next().get_next())

    def print(self):
        current = self.head
        while current.get_next() is not None:
            print(current.get_data())
            current = current.get_next()
        print(current.get_data())