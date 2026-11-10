class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maximum = 0

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][0] > height:
                h, idx = stack.pop()
                maximum = max(maximum, h * (i-idx))
                start = idx
            stack.append((height, start))
        for h, idx in stack: 
            maximum = max(maximum, h * (len(heights)-idx))
        return maximum
        