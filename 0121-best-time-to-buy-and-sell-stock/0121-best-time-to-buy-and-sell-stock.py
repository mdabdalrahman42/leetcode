class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if not prices or len(prices) < 2:
            return max_profit
        p1, p2 = 0, 1
        while p2 < len(prices):
            if prices[p2] <= prices[p1]:
                p1 = p2
            else:
                max_profit = max(max_profit, prices[p2] - prices[p1])
            p2 += 1
        return max_profit