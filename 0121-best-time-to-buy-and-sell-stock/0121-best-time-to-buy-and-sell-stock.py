class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1 = 0
        p2 = p1 + 1
        max_profit = 0
        while p2 < len(prices):
            if prices[p2] > prices[p1]:
                max_profit = max(max_profit, prices[p2] - prices[p1])
            else:
                p1 = p2
            p2 += 1
        return max_profit