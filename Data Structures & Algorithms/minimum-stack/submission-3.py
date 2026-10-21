class MinStack:

    def __init__(self):
        self.stack = []
    def push(self, val: int) -> None:
        prevMin = self.stack[-1][1] if self.stack else float('inf')
        self.stack.append(tuple((val, min(val, prevMin))))
    def pop(self) -> None:
        self.stack.pop()
    def top(self) -> int:
        return self.stack[-1][0]
    def getMin(self) -> int:
        return self.stack[-1][1]
