'''max sum of array element by 3'''
# https://leetcode.com/problems/greatest-sum-divisible-by-three/description/
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        tot_sum = sum(nums)
        if tot_sum % 3 == 0:
            return tot_sum

        remainder1, remainder2 = [], []
        for num in nums:
            if num % 3 == 1:
                remainder1.append(num)
            if num % 3 == 2:
                remainder2.append(num)

        remainder1.sort()
        remainder2.sort()

        if tot_sum % 3 == 1:
            a = remainder1[0] if remainder1 else float('inf')
            b = sum(remainder2[:2]) if len(remainder2) >= 2 else float('inf')
            return tot_sum - min(a, b)
        else:
            a = remainder2[0] if remainder2 else float('inf')
            b = sum(remainder1[:2]) if len(remainder1) >= 2 else float('inf')
            return tot_sum - min(a, b)