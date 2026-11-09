class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        result = []

        for num in nums:
            seen[num] +=1
        
        for i in range(k):
            maximum = max(seen, key = seen.get)
            result.append(maximum)
            seen.pop(maximum)
        return result 
        