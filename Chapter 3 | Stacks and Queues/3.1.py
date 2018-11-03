# ATTEMPT ONE
#
# I changed the question such that I can have an unlimited amount of
# stacks in the array. The way this works is buy having the position
# of every stacks top. Then as we pop a specific stack, we just remove
# 1 from all the affected stacks. The same logic is done for adding.

class Container(object):

    def __init__(self):
        self.container = []
        self.stack = []

    def add(self):
        self.stack.append(Stack(self.container))

    def push(self, obj=None, n=0):
        self.container.insert(self.stack[n].top, obj)
        self.stack[n].top += 1
        for i in range(n+1, len(self.stack)):
            self.stack[i].top += 1

    def pop(self, n=0):
        e = self.container.pop(self.stack[n].top-1)
        self.stack[n].top -= 1
        for i in range(n+1, len(self.stack)):
            self.stack[i].top -= 1
        return e


class Stack(object):

    def __init__(self, container=None):
        self.top = len(container)

    def inc(self):
        self.top += 1

    def dec(self):
        self.top -= 1