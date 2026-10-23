class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = {}
        
        for i in range(len(nums)):
            seen = set()
            j = i+1
            while j < len(nums):
                partner = -(nums[i]+nums[j])
                if partner in seen:
                    result[(tuple(sorted((partner, nums[i], nums[j]))))] = True
                seen.add(nums[j])
                j+=1
        return [list(t) for t in result]