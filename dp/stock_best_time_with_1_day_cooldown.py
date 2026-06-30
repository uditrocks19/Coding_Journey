from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        hold = [0] * n  # Maximum profit when holding a stock
        sold = [0] * n  # Maximum profit after selling a stock
        cooldown = [0] * n  # Maximum profit in cooldown

        # Base cases
        hold[0] = -prices[0]
        sold[0] = 0
        cooldown[0] = 0

        for i in range(1, n):
            hold[i] = max(hold[i - 1], cooldown[i - 1] - prices[i])
            sold[i] = hold[i - 1] + prices[i]
            cooldown[i] = max(cooldown[i - 1], sold[i - 1])

        # The maximum profit is in either sold or cooldown states
        return max(sold[-1], cooldown[-1])
