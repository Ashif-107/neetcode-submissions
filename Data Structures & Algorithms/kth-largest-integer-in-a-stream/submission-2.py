class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth = k
        self.hq = nums
        heapq.heapify(self.hq)
        
        while len(self.hq) > k:
            heapq.heappop(self.hq)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.hq, val)
        
        while len(self.hq) > self.kth:
            heapq.heappop(self.hq)
            
        return self.hq[0]


