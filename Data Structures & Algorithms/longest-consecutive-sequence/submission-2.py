class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        arr = set(nums)

        for i in arr:
            if i-1 not in arr:
                currentStreak = 1
                currentNum = i

                while currentNum+1 in arr:
                    currentStreak += 1
                    currentNum += 1
                longest = max(longest, currentStreak)
        return longest




        

















