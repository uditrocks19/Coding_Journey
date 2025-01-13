'''nearest point having the same coordinate'''
# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/description/
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valid_points = []
        res = []
        mx = float('inf')
        indx = -1
        for i, point in enumerate(points):
            x2, y2 = point[0], point[1]
            if not (x2 == x or y2 == y):
                continue
            else:
                d = (x-x2)**2 + (y-y2)**2
                if mx > d:
                    mx = d
                    indx = i

        return indx
