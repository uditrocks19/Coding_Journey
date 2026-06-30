''' first and last position'''
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/?envType=problem-list-v2&envId=binary-search

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first():
            l, r = 0, len(nums) - 1
            while l <= r:  # Change to l <= r
                mid = (l + r) // 2
                if nums[mid] == target:
                    r = mid - 1  # Narrow to the left side to find the first occurrence
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l if l < len(nums) and nums[l] == target else -1

        def last():
            l, r = 0, len(nums) - 1
            while l <= r:  # Change to l <= r
                mid = (l + r) // 2
                if nums[mid] == target:
                    l = mid + 1  # Narrow to the right side to find the last occurrence
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return r if r >= 0 and nums[r] == target else -1

        return [first(), last()]
