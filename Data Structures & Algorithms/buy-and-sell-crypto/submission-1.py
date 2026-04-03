class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        profit = 0
        maxprofit = 0

        for j in range(len(prices)):
            if prices[i] > prices[j]:
                i = j
            profit = prices[j] - prices[i]
            maxprofit = max(maxprofit, profit)

        return maxprofit