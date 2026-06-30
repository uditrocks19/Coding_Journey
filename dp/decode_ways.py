class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == '0':  # Edge case: starting with '0' or empty string
            return 0
        if n == 1:  # Single character that's not '0'
            return 1

        # Initialize the DP table
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            # Check if single character s[i-1] is valid
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # Check if two characters s[i-2:i] form a valid encoding
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
