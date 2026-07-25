class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hq = []
        heapq.heapify(hq)
        res = []
        for x,y in points:
            dist = x*x + y*y

            heapq.heappush(hq, (-dist, x, y))

            if len(hq) > k:
                heapq.heappop(hq)
                
        
        while hq:
            d,x,y = heapq.heappop(hq)
            res.append([x,y])
            
        return res