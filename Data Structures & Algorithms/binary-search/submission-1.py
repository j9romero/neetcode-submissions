class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start = 0
        end = n-1

        while start <= end:
            split = (start+end) //2
            if nums[split] < target:
                start = split+1
            elif nums[split] == target: 
                return split
            else: 
                end = split -1
        return -1