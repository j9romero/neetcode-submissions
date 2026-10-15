class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums: 
            counts[num] += 1

        uniqueNums = list(counts.keys()) #converting to a list
        uniqueNums.sort(key=counts.get, reverse = True)
        return uniqueNums[:k] 















        