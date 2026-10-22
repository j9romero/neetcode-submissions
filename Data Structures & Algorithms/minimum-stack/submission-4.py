class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            currentMin = min(val, self.stack[-1][1])
        else:
            currentMin = min(val, float('inf'))
        self.stack.append(tuple((val,currentMin)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
