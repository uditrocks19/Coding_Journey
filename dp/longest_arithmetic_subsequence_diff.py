'''longest increasing subsequence with adjacent diff '''
# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/
from typing import List

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # Dictionary to store the longest subsequence length ending with each number
        dp = {}
        max_length = 0

        for num in arr:
            # Calculate the previous number in the subsequence
            prev = num - difference
            # Update the current number's subsequence length
            dp[num] = dp.get(prev, 0) + 1
            # Update the maximum subsequence length
            max_length = max(max_length, dp[num])

        return max_length