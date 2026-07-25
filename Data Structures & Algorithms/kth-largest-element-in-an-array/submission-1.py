class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = []

        for x in nums:
            heapq.heappush(hq,x)

            if len(hq) > k:
                heapq.heappop(hq)
                        
        return hq[0]
