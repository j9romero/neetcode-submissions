class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        best = 1
        currentStreak = 1
        nums = sorted(set(nums))

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1:
                currentStreak += 1
            else:
                currentStreak =1
            best = max(best, currentStreak)
        return best 