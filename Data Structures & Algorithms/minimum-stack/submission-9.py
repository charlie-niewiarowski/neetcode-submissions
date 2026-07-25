class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = 0
        self.mins = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.minimum = val
        elif val < self.minimum:
            self.minimum = val

        self.stack.append(val)
        self.mins.append(self.minimum)
        print(self.stack, self.mins)

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

        if self.stack:
            self.minimum = self.mins[-1]
        else:
            self.minimum = 0

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
