'''no of subarrays with product less than k '''
# https://leetcode.com/problems/subarray-product-less-than-k/description/?envType=problem-list-v2&envId=binary-search

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        product = 1
        cnt = 0
        if k <=1:
            return 0
        n = len(nums)
        for r in range(n):
            product = product * nums[r]
            while product >= k:
                product = product // nums[l]
                l+=1

            cnt += (r - l + 1)

        return cnt
