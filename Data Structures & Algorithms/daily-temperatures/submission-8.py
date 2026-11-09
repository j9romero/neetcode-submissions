class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                prevTemp, prevIndex = stack.pop()
                result[prevIndex] = i - prevIndex
            stack.append(tuple((temp, i )))
        return result 

        