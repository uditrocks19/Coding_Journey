'''max profit with atmost 2 transactions'''
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
class Solution:
    def solve(self, index, buy, cnt, n, prices, dp):
        if index == n or cnt == 0:
            return 0
        if dp[index][buy][cnt] != -1:
            return dp[index][buy][cnt]
        
        profit = 0
        if buy:
            pick = -prices[index] + self.solve(index + 1, False, cnt, n, prices, dp)
            notPick = self.solve(index + 1, True, cnt, n, prices, dp)
            profit = max(pick, notPick)
        else:
            pick = prices[index] + self.solve(index + 1, True, cnt - 1, n, prices, dp)
            notPick = self.solve(index + 1, False, cnt, n, prices, dp)
            profit = max(pick, notPick)
        
        dp[index][buy][cnt] = profit
        return profit

    def maxProfit(self, prices):
        n = len(prices)
        dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]
        return self.solve(0, True, 2, n, prices, dp)

