class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opperands = {"+", "-", "*", "/"}

        for i, t in enumerate(tokens):
            if t not in opperands:
                stack.append(int(t))
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                #print("a:", a, "b:", b)
                if t == "+":
                    stack.append(a+b)
                if t == "-":
                    stack.append(a-b)
                if t == "*":
                    stack.append(a*b)
                if t == "/":
                    stack.append(int(a/b))
        return stack[-1]
        