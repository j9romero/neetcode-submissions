class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")":"(", "]":"[", "}":"{"}

        for par in s:
            if par in pairs:
                if stack and stack[-1] == pairs[par]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(par)
        if not stack:
            return True
        else: 
            return False
