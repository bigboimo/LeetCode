class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        res = 0

        for i in range(len(prices)):
            res = max(prices[i] - minPrice, res)
            minPrice = min(prices[i], minPrice)

        return res
            