# ATTEMPT ONE
#
# Time Complexity: O(1)
#
# Having two stacks in parallel, its much more efficient
# to store the current minimum value for every state in the
# stack. That way every min value is pre stored and the access
# time is instant.


class Stack(object):

    def __init__(self):
        self.min = []
        self.stack = []

    def push(self, val):
        if len(self.stack) == 0:
            self.min.append(val)
        elif val < self.min[len(self.min)-1]:
            self.min.append(val)
        else:
            self.min.append(self.min[len(self.min)-1])
        self.stack.append(val)

    def pop(self):
        self.min.pop(len(self.min)-1)
        return self.stack.pop(len(self.stack)-1)

    def peek(self):
        return self.stack[len(self.stack)-1]

    def get_min(self):
        return self.min[len(self.min)-1]

    def is_empty(self):
        return len(self.stack) == 0
