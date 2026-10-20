class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = n-1
        maxArea = 0
        
        while i < j:
            currentArea = min(heights[i], heights[j]) * (j-i)
            maxArea = max(maxArea, currentArea)

            if heights[i] < heights[j]:
                i +=1
            else:
                j -= 1
        return maxArea