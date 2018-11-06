# ATTEMPT ONE
#
# Time Complexity: O(n)
#
# When you pop an entire stack into another stack it becomes
# like a queue. Whenever we add we retain the stack like feature.
# When we want to go next in the queue, we cycle through the first stack
# into the second stack and pop. This results in a queue like nature.


def swap(a, b):
    if b.size == 0:
        while not a.is_empty():
            b.push(a.pop())
    else:
        while not b.is_empty():
            a.push(b.pop())


class MyQueue(object):
    def __init__(self):
        self.a = Stack()
        self.b = Stack()

    def add(self, obj):
        if self.a.size == 0:
            swap(self.a, self.b)
        self.a.push(obj)

    def next(self):
        if self.b.size == 0:
            swap(self.a, self.b)
        return self.b.pop()


class Stack(object):
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, obj):
        self.size += 1
        self.stack.append(obj)

    def pop(self):
        self.size -= 1
        return self.stack.pop(len(self.stack) - 1)

    def is_empty(self):
        return self.size == 0
