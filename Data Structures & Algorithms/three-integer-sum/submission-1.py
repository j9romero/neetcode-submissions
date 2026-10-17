class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()

        for i in range(len(nums)): 
            seen = set()
            for j in range(i+1, len(nums)):
                partner = 0 - (nums[i]+nums[j])
                if partner in seen:
                    output.add(tuple(sorted((nums[i], nums[j], partner))))
                seen.add(nums[j])
        return [list(t) for t in output]


#make it into set
#for each, look at the rest of them, subtract and see if the missing partner is there, if not, then skip and if it is then add it to output array
        