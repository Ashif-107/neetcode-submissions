class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hq = []
        heapq.heapify(hq)
        for w in stones:
            heapq.heappush(hq,-w)

        while hq:
            if len(hq) == 1:
                return -hq[0]

            x = -heapq.heappop(hq) 
            y = -heapq.heappop(hq) 

            if x == y:
                continue
            else:
                heapq.heappush(hq, -abs(y-x))
        
        return 0