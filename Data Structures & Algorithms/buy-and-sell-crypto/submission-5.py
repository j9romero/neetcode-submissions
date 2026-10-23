class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        best = 0

        for i, price in enumerate(prices):
            j = i+1
            while j < len(prices) and prices[j] > prices[i]:
                best = max(best, prices[j]-prices[i])
                j+=1
            #j+=1
        return best
                