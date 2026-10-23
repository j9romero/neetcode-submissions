class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opperators = {"+", "/", "-", "*"}

        for i in tokens:
            if i not in opperators:
                stack.append(i)
            else:
                b = int(stack.pop())
                a = int(stack.pop())

                if i == "+":
                    stack.append(a+b)
                elif i == "-":
                    stack.append(a-b)
                elif i == '*':
                    stack.append(a*b)
                else:
                    stack.append(a/b)
        return int(stack.pop())