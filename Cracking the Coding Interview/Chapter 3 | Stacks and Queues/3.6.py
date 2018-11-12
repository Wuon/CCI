# ATTEMPT ONE
#
# Time Complexity: O(1)
#
# By using two queues (one for dogs and one for cats) and by
# storing the position of entry for each animal. When we dequeue
# from animal shelter we can compare the time of entrance between
# animals, or if its a specific animal, instantly dequeue.


class Queue:
    def __init__(self):
        self.items = []
        self.size = 0;

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.size += 1
        self.items.insert(0,item)

    def dequeue(self):
        self.size -= 1
        return self.items.pop()

    def size(self):
        return self.size

    def peek(self):
        return self.items[self.size - 1]


class Cat(object):
    def __init__(self):
        self.position = 0

    def set_position(self, n):
        self.position = n


class Dog(object):
    def __init__(self):
        self.position = 0

    def set_position(self, n):
        self.position = n


class AnimalShelter(object):

    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()
        self.size = 0

    def enqueue(self, obj):
        self.size += 1
        obj.set_position(self.size)
        if type(obj).__name__ == 'Cat':
            self.cat.enqueue(obj)
        else:
            self.dog.enqueue(obj)

    def dequeue_any(self):
        if self.dog.peek().position > self.cat.peek().position:
            return self.cat.dequeue()
        return self.dog.dequeue()

    def dequeue_dog(self):
        return self.dog.dequeue()

    def dequeue_cat(self):
        return self.cat.dequeue()
