class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []

        for r, num in enumerate(nums):
            while q and q[-1][0] <= num:
                q.pop()
            q.append((nums[r],r))
            if q[0][1] <= r-k:
                q.popleft()
            if r >= k-1:
                result.append(q[0][0])
        return result 
            
                
        