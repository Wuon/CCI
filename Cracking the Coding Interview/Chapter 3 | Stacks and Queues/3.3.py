# ATTEMPT ONE
#
# The stack implementation works by checking the size of the current stack
# and if it exceeds the height amount, then we start a new stack. When we pop
# from the stack, we use the right most stack and when its empty we remove
# the stack to save space.


class SetOfStacks(object):
    def __init__(self):
        self.size = 0
        self.stackSize = 3
        self.stacks = [Stack()]

    def push(self, obj):
        if self.stacks[self.size].size >= self.stackSize:
            self.size += 1
            self.stacks.append(Stack())
        self.stacks[self.size].push(obj)

    def pop(self):
        obj = None
        if self.stacks[self.size].size <= 1:
            obj = self.stacks.pop(self.size).pop()
            self.size -= 1
        return obj if obj is not None else self.stacks[self.size].pop()


class Stack(object):
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, obj):
        self.size += 1
        self.stack.append(obj)

    def pop(self):
        self.size -= 1
        return self.stack.pop(len(self.stack)-1)
