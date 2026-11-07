class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        best = 0
        seen = set()
        streak = 0

        for i in nums:
            seen.add(i)
            if i-1 not in seen:
                streak = 1
            else:
                streak += 1
            best = max(best, streak)
            
        return best
        