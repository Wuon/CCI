# ATTEMPT ONE
#
# Time Complexity: O(n^2)
#
# Without using any other data structures, by temporarily holding
# the popped value from stack 1, we can continuously pop from stack 2
# right until we hit a number that is lower than the one we are holding.
# Then since we know how many times we popped from stack two, we can push
# them back into stack 2, retaining the order. Unfortunately this type of
# approach is bound to be inefficient and is given a runtime of O(n^2)


def sort_stack(s):
    s2 = Stack()
    s2.push(s.pop())
    while not s.is_empty():
        if s.peek() <= s2.peek():
            s2.push(s.pop())
        else:
            t = s.pop()
            c = 0
            while not s2.is_empty() and s2.peek() < t:
                s.push(s2.pop())
                c += 1
            s2.push(t)
            for i in range(0, c):
                s2.push(s.pop())
    return s2


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

    def peek(self):
        return self.stack[self.size-1]

    def is_empty(self):
        return self.size == 0
