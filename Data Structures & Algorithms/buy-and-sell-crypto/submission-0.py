class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for n in prices[1:]:
            max_profit = max(max_profit, n - min_price)
            min_price = min(n, min_price)

        return max_profit
