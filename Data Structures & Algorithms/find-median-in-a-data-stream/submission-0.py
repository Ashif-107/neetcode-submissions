class MedianFinder:

    def __init__(self):
        self.maxheap = [] #left part of stream
        heapq.heapify(self.maxheap)
        self.minheap = [] #right part of stream
        heapq.heapify(self.minheap)

        self.count = 0

    def addNum(self, num: int) -> None:
        if not self.maxheap or  num  <= -self.maxheap[0]:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)
        
        if len(self.maxheap) > len(self.minheap) + 1:
            x = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, x)
        elif len(self.minheap) > len(self.maxheap):
            x = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -x)


    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        else:
            maxx = -self.maxheap[0]
            minn = self.minheap[0]
            return ((maxx+minn)/ 2)