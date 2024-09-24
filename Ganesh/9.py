class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice, profit = prices[0], 0
        for i in range(len(prices)):
            if prices[i] < buyPrice:
                buyPrice = prices[i]
            elif prices[i] > buyPrice :
                profit += prices[i] - buyPrice
                buyPrice = prices[i]
        return profit