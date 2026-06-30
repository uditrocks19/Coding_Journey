class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)
        if sm % 2:
            return False
        sm //= 2
        n = len(nums)
        dp = [[False] * (sm + 1) for _ in range(n + 1)]
        for i in range(sm + 1):
            dp[0][i] = False

        for i in range(1, n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, sm + 1):
                dp[i][j] = dp[i - 1][j]
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i][j] | dp[i - 1][j - nums[i - 1]]
        return dp[n][sm]