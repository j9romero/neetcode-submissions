class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0]*len(height)
        currMax = 0
        for i, h in enumerate(height):
            currMax = max(currMax, h)
            leftMax[i] = currMax
        
        currMax = 0
        rightMax = [0]*len(height)
        for i in range(len(height)-1, -1, -1):
            currMax = max(currMax, height[i])
            rightMax[i] = currMax

        total = 0
        for i, h in enumerate(height):
            water = min(leftMax[i], rightMax[i]) - h
            total+=water 
        return total
            