class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = 0
        left = [0]*len(height)
        for l, tall in enumerate(height):
            if tall > leftMax:
                leftMax = tall
                left[l] = leftMax
            else:
                left[l] = leftMax
        
        right = [0]*len(height)
        rightMax = 0
        for r in range(len(height)-1, -1, -1):
            if height[r] > rightMax:
                rightMax = height[r]
            right[r] = rightMax
        
        total = 0
        for i in range(len(height)):
            total += min(left[i], right[i]) - height[i]
        return total 

        