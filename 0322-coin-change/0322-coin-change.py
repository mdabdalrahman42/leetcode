class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0:0}
        def dfs(curr_sum):
            if curr_sum in dp:
                return dp[curr_sum]
            if curr_sum < 0:
                return -1
            min_coins = float("inf")
            for coin in coins:
                res = dfs(curr_sum - coin)
                if res != -1:
                    min_coins = min(min_coins, 1 + res)
            dp[curr_sum] = min_coins if min_coins != float("inf") else -1
            return dp[curr_sum]
        output = dfs(amount)
        return output if output != -1 else -1