class MinStack:

    def __init__(self):
        self.stack = []
    def push(self, val: int) -> None:
        if self.stack:
            currentMin = min(self.stack[-1][1], val)
        else:
            currentMin = val
        self.stack.append((val, currentMin))
    def pop(self) -> None:
        self.stack.pop()
    def top(self) -> int:
        return self.stack[-1][0]
    def getMin(self) -> int:
        return self.stack[-1][1]
