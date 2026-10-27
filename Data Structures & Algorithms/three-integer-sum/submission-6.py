class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = set()

        for i in range(len(nums)):
            seen = set()
            for j in range(i+1, len(nums)):
                partner = -(nums[i]+nums[j])
            
                if partner in seen:
                    result.add(tuple(sorted((partner, nums[i], nums[j]))))
                seen.add(nums[j])
        return [list(t) for t in result]