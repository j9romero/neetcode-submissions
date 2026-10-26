class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                difference = i-stack[-1]
                result[stack[-1]] = difference
                stack.pop()
            stack.append(i)
        return result 