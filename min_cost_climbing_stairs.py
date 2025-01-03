'''leetcode min_cost climbing stairs'''
import copy


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def result(dp, idx=0):
            dp = dp[idx:]
            dp.append(0)
            n = len(dp)
            res = [float('inf')] * (n)
            if n <= 1:
                return 0
            res[0] = 0
            res[1] = dp[0]
            for i in range(2, n):
                res[i] = min(res[i - 1] + dp[i - 1], res[i - 2] + dp[i - 2])
            return res[n - 1]

        n = len(cost)
        if n == 1:
            return 0
        return min(result(copy.copy(cost), 0), result(copy.copy(cost), 1))

