class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(numbers):
            partner = target - num
            if partner in seen:
                return [seen[partner]+1, i+1]
            seen[num] = i
        

    