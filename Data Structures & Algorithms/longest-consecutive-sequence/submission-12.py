class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        #print(nums)
        seen = set()
        if not nums:
            return 0
        best = 0
        currentStreak = 0

        for i, num in enumerate(nums):
            seen.add(num)
            if num-1 not in seen:
                currentStreak = 1
            else:
                currentStreak +=1
            best = max(currentStreak, best)
            #print(best)
        return best