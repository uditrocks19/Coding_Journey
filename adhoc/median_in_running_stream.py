# median in a runnning stream using heap max heap storing lower half of the elements and max heap storing the right half
import heapq

class MedianStream:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def add_num(self, num):
        if not self.max_heap  or num <= -1 * self.max_heap[0]:
            heapq.heappush(self.max_heap, -1 * num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -1 *heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -1 * heapq.heappop(self.min_heap))

    def find_median(self):
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        else:
            return float((-self.max_heap[0] + self.min_heap[0])/2)

obj = MedianStream()
obj.add_num(1)
obj.add_num(2)
print(obj.find_median())
obj.add_num(7)
print(obj.find_median())
