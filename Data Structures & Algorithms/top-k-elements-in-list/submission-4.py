class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numSet = defaultdict(int)

        for i in nums:
            numSet[i] +=1

        return sorted(numSet, key = numSet.get, reverse = True)[:k]
        
































        