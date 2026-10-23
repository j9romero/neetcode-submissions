class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        dict = defaultdict(int)


        for i, num in enumerate(nums):
            dict[num] +=1
        
        for i in range(k):
            best = max(dict, key = dict.get)
            result.append(best)
            del dict[best]
        
        return result