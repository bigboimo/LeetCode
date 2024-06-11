class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) < 2:
            return 0

        maxProfit = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)
            else: 
                l = r
            r += 1
        return maxProfit