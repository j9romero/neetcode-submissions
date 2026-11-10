class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")":"(", "}":"{", "]":"["}
        stack = []

        for par in s:
            if par in pairs:
                if not stack or pairs[par] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(par)
        return not stack
        