class Solution:
    def maxArea(self, heights: List[int]) -> int:
        biggest = 0
        i = 0
        j= len(heights) -1
        while i < j: 
            length = j-i
            area = length* (min(heights[i], heights[j]))
            biggest = max(biggest, area)

            if heights[i] < heights[j]:
                i +=1
            else:
                j -=1
        return biggest


#algorithm:
#start from two pointers going inward, calculating the container area using the smallest height of them and multiplying by how far apart they are, and compare with the max area each time
#we can move the index from the smaller height because the smaller one's area is maxed out and moving the other pointer would only make the area smaller, if both are the same then move either