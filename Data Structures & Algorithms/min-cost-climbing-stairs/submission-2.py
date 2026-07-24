class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        mc = [float("inf")] * (n+1)
        mc[0] = 0
        mc[1] = 0

        for i in range(2,n+1):
            mc[i] = min(mc[i-1]+cost[i-1], mc[i-2]+cost[i-2])
        
        
        return mc[n]