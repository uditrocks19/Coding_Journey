'''Find k closest element to a number in x in a sorted array'''
import heapq


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k > len(arr):
            return []
        if k == len(arr):
            return arr
        min_heap = []
        for i, num in enumerate(arr):
            heapq.heappush(min_heap, (abs(num - x), i))

        res = []
        while k > 0:
            index = heapq.heappop(min_heap)[1]
            res.append(arr[index])
            k -= 1
        res.sort()
        return res