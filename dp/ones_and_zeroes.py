'''ones and zeros with atmost m zeroes and n ones'''
# https://leetcode.com/problems/ones-and-zeroes/description/
from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def helper(s):
            return (s.count('0'), s.count('1'))

        dp = {}

        def solve(index, cnt0, cnt1):
            # Base case: If all strings are considered or limits are exceeded
            if index == len(strs):
                return 0
            if (index, cnt0, cnt1) in dp:
                return dp[(index, cnt0, cnt1)]

            a, b = helper(strs[index])

            # Choice 1: Include the current string if possible
            include = 0
            if cnt0 + a <= m and cnt1 + b <= n:
                include = 1 + solve(index + 1, cnt0 + a, cnt1 + b)

            # Choice 2: Exclude the current string
            exclude = solve(index + 1, cnt0, cnt1)

            # Store the result in the memoization table
            dp[(index, cnt0, cnt1)] = max(include, exclude)
            return dp[(index, cnt0, cnt1)]

        return solve(0, 0, 0)
