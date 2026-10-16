class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        ordered = sorted(counts, key=counts.get, reverse =True)
        return ordered[:k]






























        