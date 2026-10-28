class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        minRate = end

        while start <= end:
            mid = (start + end)// 2
            hours = 0
            for p in piles:
                hours += (p+mid-1) //mid
            
            if hours <= h:
                minRate = mid
                end = mid - 1
            else:
                start = mid + 1
        return minRate
        