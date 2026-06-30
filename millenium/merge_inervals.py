'''merge intervals'''
# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        n = len(intervals)
        if n == 1:
            return intervals

        merge = [intervals[0]]
        for i in range(1, n):
            curr_start, curr_end = intervals[i][0], intervals[i][1]
            prev_start, prev_end = merge[-1][0], merge[-1][1]
            if curr_start <= prev_end:
                merge[-1][1] = max(curr_end, prev_end)
            else:
                merge.append(intervals[i])

        return merge
