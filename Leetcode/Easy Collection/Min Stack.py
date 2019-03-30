class MinStack:

    def __init__(self):
        self.min = []
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.min) == 0 or x < self.min[len(self.min) - 1]:
            self.min.append(x)
        else:
            self.min.append(self.min[len(self.min) - 1])
        self.stack.append(x)

    def pop(self) -> None:
        d = self.stack[len(self.stack) - 1]
        self.stack = self.stack[:-1]
        self.min = self.min[:-1]
        return d

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        if len(self.min) != 0:
            return self.min[len(self.min) - 1]
