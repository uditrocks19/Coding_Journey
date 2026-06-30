class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1

        product = 1
        while n > 4:
            product *= 3
            n = n - 3

        return product * n

# Dynamic programming approach
def integer_break(n):
    # DP array to store the maximum product for each number
    dp = [0] * (n + 1)
    dp[1] = 0  # Base case: no product possible for 1

    for i in range(2, n + 1):  # Start computing for numbers 2 to n
        for j in range(1, i):  # Split i into j and (i-j)
            dp[i] = max(dp[i], max(j, dp[j]) * max(i - j, dp[i - j]))

    return dp[n]


# Example usage
def integer_break(n):
    # DP array to store the maximum product for each number
    dp = [0] * (n + 1)
    dp[1] = 0  # Base case: no product possible for 1

    for i in range(2, n + 1):  # Start computing for numbers 2 to n
        for j in range(1, i):  # Split i into j and (i-j)
            dp[i] = max(dp[i], max(j, dp[j]) * max(i - j, dp[i - j]))

    return dp[n]


# Example usage
def integer_break(n):
    # DP array to store the maximum product for each number
    dp = [0] * (n + 1)
    dp[1] = 0  # Base case: no product possible for 1

    for i in range(2, n + 1):  # Start computing for numbers 2 to n
        for j in range(1, i):  # Split i into j and (i-j)
            dp[i] = max(dp[i], max(j, dp[j]) * max(i - j, dp[i - j]))

    return dp[n]


# Example usage
def integer_break(n):
    # DP array to store the maximum product for each number
    dp = [0] * (n + 1)
    dp[1] = 0  # Base case: no product possible for 1

    for i in range(2, n + 1):  # Start computing for numbers 2 to n
        for j in range(1, i):  # Split i into j and (i-j)
            dp[i] = max(dp[i], max(j, dp[j]) * max(i - j, dp[i - j]))

    return dp[n]


# Example usage
def integer_break(n):
    # DP array to store the maximum product for each number
    dp = [0] * (n + 1)
    dp[1] = 0  # Base case: no product possible for 1

    for i in range(2, n + 1):  # Start computing for numbers 2 to n
        for j in range(1, i):  # Split i into j and (i-j)
            dp[i] = max(dp[i], max(j, dp[j]) * max(i - j, dp[i - j]))

    return dp[n]

