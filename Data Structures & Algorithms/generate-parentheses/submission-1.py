class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current, openCount, closedCount):
            if len(current) == 2* n:
                result.append(current)
                return
            if openCount < n:
                backtrack(current + "(", openCount+1, closedCount)
            if closedCount < openCount: 
                backtrack(current+ ")", openCount, closedCount+1)
        backtrack("", 0, 0)
        return result
