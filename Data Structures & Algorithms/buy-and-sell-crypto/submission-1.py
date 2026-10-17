class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0

        for i, val in enumerate(prices):
            for j in range(i+1, len(prices)):
                profit = prices[j] -prices[i]
                best = max(best, profit)
        return best



#check all of the summations possible after the index you are currently at, should be less and less for each


        