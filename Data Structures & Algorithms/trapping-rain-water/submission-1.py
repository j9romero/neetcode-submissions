class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0]*n
        maxRight = [0]*n

        left = 0
        for i in range(n):
            left = max(left, height[i])
            maxLeft[i] = left
        
        right = 0
        for i in range(n-1, -1, -1): 
            right = max(right, height[i])
            maxRight[i] = right
        
        best = 0
        for i in range(n):
            water = min(maxLeft[i], maxRight[i]) - height[i]
            best +=water
        return best





#start at first number where the number after is smaller
#start at last number where the number before was smaller
#can only contain water in a dip where you have numbers getting smaller and then getting bigger, once the bigger number starts to get smaller then you know you have water in between the biggest and the start, with whichever is shortest being where the water starts

#for each is min of max left and max right and then you subtract the height at that index and add it all to water total because that is how much water can be stored directly over that unit