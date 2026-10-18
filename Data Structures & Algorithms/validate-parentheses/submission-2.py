class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = { ')': '(', ']': '[', '}': '{' }

        for i in s: 
            if i in pairs:
                if not stack or stack[-1] != pairs[i]: #checking its pair
                    return False #if top not its pair return false
                stack.pop()
            else:
                stack.append(i)

        return not stack
        