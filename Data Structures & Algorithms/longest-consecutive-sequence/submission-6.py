class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = sorted(set(nums))
        currentStreak = 0
        seen = {}

        for i in numSet:
            if i-1 not in seen:
                currentStreak = 1
            else:
                currentStreak += 1
            seen[i] = 1
            longest = max(currentStreak, longest)
        return longest