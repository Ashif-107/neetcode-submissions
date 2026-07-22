class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        now = [-1,-1,-1]

        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                now[0] = max(now[0], a)
                now[1] = max(now[1], b)
                now[2] = max(now[2], c)

        return now == target
            
        
