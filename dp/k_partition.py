'''leetcode 1043'''


def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)  # DP array to store the maximum sum for subarray arr[0:i]

    for i in range(1, n + 1):
        max_val = 0
        # Iterate over subarray lengths (1 to k)
        for j in range(1, min(k, i) + 1):
            max_val = max(max_val, arr[i - j])  # Max value in the current subarray
            dp[i] = max(dp[i], dp[i - j] + max_val * j)  # Update dp[i]

    return dp[n]


# Example usage:
arr = [1, 15, 7, 9, 2, 5, 10]
k = 3
print(maxSumAfterPartitioning(arr, k))  # Output: 84
