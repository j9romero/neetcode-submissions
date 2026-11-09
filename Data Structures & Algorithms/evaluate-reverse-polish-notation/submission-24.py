class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ["+", "-", "/", "*"]

        for numbers in tokens:
            if numbers not in operands:
                stack.append(int(numbers))
            else:
                b = int(stack.pop())
                a = int(stack.pop())

                if numbers == "+":
                    stack.append(a+b)
                elif numbers == "-":
                    stack.append(a-b)
                elif numbers == "*":
                    stack.append(a*b)
                elif numbers == "/":
                    stack.append(int(a/b))
        return stack.pop()
        