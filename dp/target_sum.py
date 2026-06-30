'''target sum '''
# https://leetcode.com/problems/target-sum/description/
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # Edge case: if the absolute value of target is greater than the total sum of nums
        if abs(target) > sum(nums):
            return 0

        dp = {}

        def helper(i, curr_sum):
            # Base case: If all numbers are used
            if i == n:
                return 1 if curr_sum == target else 0

            # Check memoization table
            if (i, curr_sum) in dp:
                return dp[(i, curr_sum)]

            # Recursive calls: Add or subtract the current number
            add = helper(i + 1, curr_sum + nums[i])
            subtract = helper(i + 1, curr_sum - nums[i])

            # Store the result in memoization table
            dp[(i, curr_sum)] = add + subtract
            return dp[(i, curr_sum)]

        return helper(0, 0)

