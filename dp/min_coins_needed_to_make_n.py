class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(1, amount + 1):
                if i >= coin and dp[i - coin] != float('inf'):
                    dp[i] = min(dp[i - coin] + 1, dp[i])

        return dp[amount] if dp[amount] != float('inf') else -1
