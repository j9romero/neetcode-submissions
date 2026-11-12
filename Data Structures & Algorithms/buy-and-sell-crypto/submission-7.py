class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 0
        best = 0

        for l, price in enumerate(prices):
            for r in range(l+1, len(prices)):
                if prices[r] > price:
                    best = max(best, prices[r]-price)
        return best
